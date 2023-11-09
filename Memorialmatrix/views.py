import json
import traceback
from django.http import JsonResponse
from django.shortcuts import render
from django.template.defaultfilters import upper
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from itertools import chain
from rest_framework import permissions
from itertools import chain
from rest_framework import permissions
from .serializers import MemorialSerializer
from .models import *
from django.db import connection
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings
from rest_framework.pagination import PageNumberPagination
import time
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail
from django.conf import settings
from liquid import Template
import logging


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def medialink_list(request):
    if request.method == 'GET':
        db_name = connection.settings_dict['ENGINE']
        if "postgresql" in db_name:
            medialinks = MediaLinks.objects.raw(
                'SELECT * FROM "Memorialmatrix_medialinks" WHERE medialinks_approval = true;')
        else:
            medialinks = MediaLinks.objects.raw(
                'SELECT * FROM Memorialmatrix_medialinks WHERE medialinks_approval == 1;')

        raw_id_list = []
        for each_medialinks in medialinks:
            if each_medialinks.id not in raw_id_list:
                raw_id_list.append(each_medialinks.id)
        pre_medialinks_list = []
        medialink = MediaLinks.history.model
        if "postgresql" in db_name:
            medialinks_list = medialink.objects.raw(
                'SELECT DISTINCT ON ("id") * FROM "History_MediaLinks" WHERE medialinks_approval = true ORDER BY "id", "history_date" DESC;')
        else:
            medialinks_list = medialink.objects.raw(
                'SELECT * FROM History_MediaLinks WHERE medialinks_approval == 1 GROUP BY id HAVING MAX(history_date);')

        for each_medialinks in medialinks_list:
            if each_medialinks.id not in raw_id_list:
                pre_medialinks_list.append(each_medialinks)

        current_medialinks = MediaLinks.objects.filter(medialinks_approval=True)
        result_list = list(chain(pre_medialinks_list, current_medialinks))
        serializer = MediaLinksSerializer(result_list, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = MediaLinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_approved_count(request):
    approved_count = Memorial.objects.filter(is_approved='approved').count()
    return Response({'data': approved_count})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def website_configuration_parameter(request, parameter_name):
    parameter = WebsiteConfigParameter.objects.filter(parameter_name=parameter_name, is_enabled='True')
    if parameter.exists():
        return Response({'data': parameter.get().parameter_value})
    return Response({'data': None})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_profile_photo(request, mem_id):
    memorial = Memorial.objects.filter(id=mem_id)

    if memorial.exists():
        photo_urls = []
        if memorial.get().profile_picture is not None:
            photo_urls.append(memorial.get().profile_picture)

        media_links = MediaLinks.objects.filter(mem_medialinks_id=mem_id, type='photo').all()
        for each_media_link in media_links:
            photo_urls.append(each_media_link.url)

        if len(photo_urls) == 0:
            parameter = WebsiteConfigParameter.objects\
                .filter(parameter_name='MEMORIAL_DEFAULT_PICTURE_URL', is_enabled='True')
            if parameter.exists():
                photo_urls.append(parameter.get().parameter_value)

        updated_photo_urls = []
        for photo_url in photo_urls:
            if photo_url != '' and photo_url is not None:
                photo_url = photo_url.strip()
                if not photo_url.startswith("http"):
                    photo_url = "https://" + photo_url
                updated_photo_urls.append(photo_url)

    return Response({'data': updated_photo_urls})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_upcoming_events(request):
    db_name = connection.settings_dict['ENGINE']
    if "postgresql" in db_name:
        locations = Location.objects.raw(
            'SELECT * FROM "Memorialmatrix_location" WHERE time_active_start >= CURRENT_DATE;')
    else:
        locations = Location.objects.raw('SELECT * FROM Memorialmatrix_location WHERE time_active_start >= DATE() ;')

    raw_id_list = []
    for each_location in locations:
        if each_location.id not in raw_id_list:
            raw_id_list.append(each_location.id)

    memorials = []
    if len(raw_id_list) > 0:
        memorials = Memorial.objects.raw('SELECT * FROM "Memorialmatrix_memorial" WHERE "mem_location_id" in %s;',
                                         [tuple(raw_id_list)])

    serializer = MemorialSerializer(memorials, many=True)
    return Response({'data': serializer.data})


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_featured_memorials(request):
    memorials = Memorial.objects.filter(is_approved='approved', is_featured='True').order_by("-last_modified")[:15]
    serializer = MemorialSerializer(memorials, many=True)
    return Response({'data': serializer.data})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_list(request):
    if request.method == 'GET':
        current_memorials = Memorial.objects.filter(is_approved='approved')
        query = request.GET.get('searchName')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(name__icontains=query))
        query = request.GET.get('searchFounderName')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(founder_name__icontains=query))
        query = request.GET.get('searchCity')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(mem_location__city__icontains=query))
        query = request.GET.get('searchState')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(mem_location__state__icontains=query))
        query = request.GET.get('searchZip')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(mem_location__zipcode__icontains=query))
        query = request.GET.get('searchType')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(type__icontains=query))
        query = request.GET.get('searchStartDate')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(mem_location__time_active_start__icontains=query))
        query = request.GET.get('searchEndDate')
        if (query and len(query) > 0):
            current_memorials = current_memorials.filter(Q(mem_location__time_active_end__icontains=query))

        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(current_memorials, request)
        serializer = MemorialSerializer(result_page, context={'request': request}, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = MemorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StandardResultsSetPagination(PageNumberPagination):
    # Reference: https://www.django-rest-framework.org/api-guide/pagination/
    page_size = 10
    page_size_query_param = 'page_size'


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def location_list(request):
    db_name = connection.settings_dict['ENGINE']
    if "postgresql" in db_name:
        locations = Location.objects.raw('SELECT * FROM "Memorialmatrix_location" WHERE location_approval = true;')
    else:
        locations = Location.objects.raw('SELECT * FROM Memorialmatrix_location WHERE location_approval == 1;')

    raw_id_list = []
    for each_location in locations:
        if each_location.id not in raw_id_list:
            raw_id_list.append(each_location.id)
    pre_location_list = []
    location = Location.history.model
    if "postgresql" in db_name:
        location_list = location.objects.raw(
            'SELECT DISTINCT ON ("id") * FROM "History_Location" WHERE location_approval = true ORDER BY "id", "history_date" DESC;')
    else:
        location_list = location.objects.raw(
            'SELECT * FROM History_Location WHERE location_approval == 1 GROUP BY id HAVING MAX(history_date);')

    for each_location in location_list:
        if each_location.id not in raw_id_list:
            pre_location_list.append(each_location)

    current_locations = Location.objects.filter(location_approval=True)
    result_list = list(chain(pre_location_list, current_locations))

    if request.method == 'GET':
        serializer = LocationSerializer(result_list, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def memorial_detail_view(request, id):
    try:
        if request.method == 'GET':
            id = id.replace('-', '')
            approved_memorial = Memorial.objects.filter(id=id, is_approved='approved').exists()

            if approved_memorial == True:
                now_approved_memorial = Memorial.objects.get(id=id)
                serializer = MemorialSerializer(now_approved_memorial)
                return Response(serializer.data)

            db_name = connection.settings_dict['ENGINE']
            memorial = Memorial.history.model
            location = Location.history.model

            if "postgresql" in db_name:
                memorial_list = memorial.objects.raw(
                    'SELECT m.id AS mem_id, m.history_id, m."name" AS mem_name, m.type AS mem_type, m.founder_name, m.email, m.profile_picture, m.google_virtual_tour, m.website, m.description, m.social_media_twitter, m.social_media_instagram, m.social_media_facebook FROM "History_Memorial" m JOIN "History_Location" l ON m.mem_location_id = l.id WHERE "is_approved"= %s AND m.id=%s ORDER BY m.history_date DESC LIMIT 1;',
                    ['approved', id])
            else:
                memorial_list = memorial.objects.raw(
                    'SELECT m.id AS mem_id, l.id AS loc_id, m.history_id, m.name, m.type AS mem_type, m.founder_name, m.email, m.profile_picture, m.google_virtual_tour, m.website, m.description, m.social_media_twitter, m.social_media_instagram, m.social_media_facebook FROM History_Memorial m JOIN "History_Location" l ON m.mem_location_id = l.id WHERE m.is_approved == "approved" AND m.id==%s ORDER BY m.history_date DESC LIMIT 1',
                    [id])

            memorial = Memorial.objects.get(id=id)
            location_id = memorial.mem_location_id
            location_id = str(location_id).replace('-', '')
            location_list = []

            if "postgresql" in db_name:
                location_list = location.objects.raw(
                    'SELECT l.id AS loc_id, l.history_id, l.address, l.city, l.state, l.zipcode, l.time_active_start, l.time_active_end, l.lat_coord, l.long_coord, l.permanent FROM "History_Location" l WHERE l.id=%s ORDER BY l.history_date DESC LIMIT 1',
                    [location_id])

            else:
                location_list = location.objects.raw(
                    'SELECT l.id, l.history_id, l.address, l.city, l.state, l.zipcode, l.time_active_start, l.time_active_end, l.lat_coord, l.long_coord, l.permanent FROM History_Location l WHERE l.id=%s ORDER BY l.history_date DESC LIMIT 1',
                    [location_id])

            m_list = {}
            l_list = {}

            for loc in location_list:
                if location_id is None:
                    l_list = {"id": "",
                              "address": "",
                              "city": "",
                              "state": "",
                              "zipcode": "",
                              "time_active_start": "",
                              "time_active_end": "",
                              "lat_coord": "",
                              "long_coord": "",
                              "permanent": ""
                              }
                else:
                    l_list = {"id": loc.id,
                              "address": loc.address,
                              "city": loc.city,
                              "state": loc.state,
                              "zipcode": loc.zipcode,
                              "time_active_start": loc.time_active_start,
                              "time_active_end": loc.time_active_end,
                              "lat_coord": loc.lat_coord,
                              "long_coord": loc.long_coord,
                              "permanent": loc.permanent
                              }

            for mem in memorial_list:
                m_list = {
                    "id": mem.mem_id,
                    "type": mem.type,
                    "founder_name": mem.founder_name,
                    "name": mem.name,
                    "email": mem.email,
                    "profile_picture": mem.profile_picture,
                    "google_virtual_tour": mem.google_virtual_tour,
                    "website": mem.website,
                    "description": mem.description,
                    "social_media_twitter": mem.social_media_twitter,
                    "social_media_instagram": mem.social_media_instagram,
                    "social_media_facebook": mem.social_media_facebook,
                    "mem_location": l_list
                }

            json.dumps(m_list, cls=DjangoJSONEncoder)
            serializer = MemorialSerializer(m_list)
            print(m_list)
            print(serializer.data)
            return Response(serializer.data)

    except Memorial.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def memorialDetail(request, pk):
    memorial = Memorial.objects.get(id=pk)
    serializer = MemorialSerializer(memorial, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def memorial_map_List(request):
    db_name = connection.settings_dict['ENGINE']
    if "postgresql" in db_name:
        memorials = Memorial.objects.raw('SELECT * FROM "Memorialmatrix_memorial" WHERE "is_approved"=%s;',
                                         ['approved'])

    else:
        memorials = Memorial.objects.raw('SELECT * FROM Memorialmatrix_memorial WHERE is_approved =="approved";')
    raw_id_list = []
    for each_memorial in memorials:
        if each_memorial.id not in raw_id_list:
            raw_id_list.append(each_memorial.id)

    pre_memorial_list = []
    memorial = Memorial.history.model
    if "postgresql" in db_name:
        memorial_list = memorial.objects.raw(
            'SELECT DISTINCT ON ("id") * FROM "History_Memorial" WHERE "is_approved"= %s ORDER BY "id", "history_date" DESC;',
            ['approved'])
    else:
        memorial_list = memorial.objects.raw(
            'SELECT * FROM History_Memorial WHERE is_approved == "approved" GROUP BY id HAVING MAX(history_date);')

    for each_memorial in memorial_list:
        if each_memorial.id not in raw_id_list:
            pre_memorial_list.append(each_memorial)

    current_memorials = Memorial.objects.filter(is_approved='approved')
    result_list = list(chain(pre_memorial_list, current_memorials))

    if request.method == 'GET':
        serializer = MemorialMapSerializer(result_list, context={'request': request}, many=True)
        return Response({'data': serializer.data})


@api_view(['POST', 'PUT'])
@permission_classes((permissions.AllowAny,))
def medialinkCreateOrUpdate(request):
    print(request.data)
    if request.method == 'POST':
        return mediaLinksCreate(request)
    if request.method == 'PUT':
        MediaLinks.objects.filter(mem_medialinks=request.data.get('memorial')).delete()
        return mediaLinksCreate(request)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def memorialCreate(request):
    print(request.data)
    global admin_approval_email
    serializer = MemorialCreateSerializer(data=request.data)
    if serializer.is_valid():
        admin_approval_email_obj = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_ADMIN_APPROVAL',
                                                                          is_enabled='True')
        parameter = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_MESSAGE_MEMORIAL_ADMIN_APPROVAL')
        if parameter.exists():
            message = parameter.get().parameter_value
        else:
            memorial_name = request.data.get('name')
            memorial_founder_name = request.data.get('founder_name')
            memorial_description = request.data.get('description')
            message = f'The following memorial is ready for review: {memorial_name}\nMemorial Description: {memorial_description}\nMemorial Founder Name: {memorial_founder_name}'
        if admin_approval_email_obj.exists():
            admin_approval_email = admin_approval_email_obj.get().parameter_value

        memorial_name = request.data.get('name')
        memorial_founder_name = request.data.get('founder_name')
        memorial_description = request.data.get('description')
        email = request.data.get('email')
        template = Template(message)
        final_message = template.render(mem_name=memorial_name, memfounder_name=memorial_founder_name, mem_description=memorial_description)
        subject = f'Memorial Approval Needed: {memorial_name}'
        try:
            send_mail(subject, final_message, from_email=email, recipient_list=[admin_approval_email])
        except:
            logging.exception(
                "The application configuration parameter is not set in Memorialmatrix_WebsiteConfigParameter table.")

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
# @permission_classes((permissions.AllowAny,))
def memorialUpdate(request, pk):
    try:
        memorial = Memorial.objects.get(id=pk)
    except Memorial.DoesNotExist:
        return JsonResponse({'message': 'The Memorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MemorialUpdateSerializer(memorial, data=request.data)
    if serializer.is_valid():
        serializer.update(memorial, serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def memorialMediaLinks(request, mem_id):
    medialinks = MediaLinks.objects.filter(mem_medialinks_id=mem_id)
    serializer = MediaLinkByMemorialSerializer(medialinks, many=True)
    return Response(serializer.data)


wait_once = 0


def mediaLinksCreate(request):
    try:
        global wait_once
        if wait_once == 0:
            time.sleep(2)
            wait_once = wait_once + 1
        memorial = Memorial.objects.get(id=request.data.get('memorial'))
        for key, value in request.data.items():
            if key == 'photoLinks' and len(value) > 0:
                for photo in value:
                    url = photo.get('purl')
                    if url != '':
                        MediaLinks.objects.create(url=url, type='photo', mem_medialinks=memorial)

            if key == 'videoLinks' and len(value) > 0:
                for video in value:
                    url = video.get('vurl')
                    if url != '':
                        MediaLinks.objects.create(url=url, type='video', mem_medialinks=memorial)

            if key == 'pressLinks' and len(value) > 0:
                for press in value:
                    url = press.get('pcurl')
                    if url != '':
                        MediaLinks.objects.create(url=url, type='press coverage',
                                                  mem_medialinks=memorial)
        print('Media Links save Successful')
        return Response(status=status.HTTP_201_CREATED)

    except:
        traceback.print_exc()
        print('media links save failed')
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def contactUs(request):
    global general_inquiry_email
    global media_inquiry_email
    global research_inquiry_email
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        general_inquiry_email_obj = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_GENERAL_INQUIRY', is_enabled='True')
        media_inquiry_email_obj = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_MEDIA_INQUIRY', is_enabled='True')
        research_inquiry_email_obj = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_RESEARCH_INQUIRY', is_enabled='True')
        if general_inquiry_email_obj.exists():
            general_inquiry_email = general_inquiry_email_obj.get().parameter_value
        if media_inquiry_email_obj.exists():
            media_inquiry_email = media_inquiry_email_obj.get().parameter_value
        if research_inquiry_email_obj.exists():
            research_inquiry_email = research_inquiry_email_obj.get().parameter_value

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        inquiry = request.data.get('inquiry')
        email = request.data.get('email')
        msg = request.data.get('message')
        subject = f'{inquiry} received from {first_name} {last_name}'
        message = f'Inquiry from: {email}\nMessage: {msg}'

        try:
            if inquiry == 'General Inquiry':
                send_mail(subject, message, from_email=email, recipient_list=[general_inquiry_email])
            elif inquiry == 'Media Inquiry':
                send_mail(subject, message, from_email=email, recipient_list=[media_inquiry_email])
            else:
                send_mail(subject, message, from_email=email, recipient_list=[research_inquiry_email])
        except:
            logging.exception("The application configuration parameters are not set in Memorialmatrix_WebsiteConfigParameter table.")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        logging.error("No data received from service response.")
        return Response(serializer.errors(), status=status.HTTP_400_BAD_REQUEST)
