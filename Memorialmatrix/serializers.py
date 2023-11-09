from rest_framework import serializers
from .models import *


# from .models import Memorial

class MediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLinks
        fields = (
            'id', 'mem_medialinks',
            'type', 'url')
        depth = 1


class MediaLinkByMemorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLinks
        fields = ('id', 'type', 'url')


class WebUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebUser
        fields = (
            'first_name', 'last_name', 'email', 'email_updates',
            'zipcode', 'web_user_loss', 'web_user_affiliated')
        depth = 1


class MemorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memorial
        fields = (
            'id', 'name', 'type', 'memorial_day_observance', 'memorial_type_desc', 'founder_name', 'email', 'profile_picture',
            'google_virtual_tour', 'website', 'description', 'social_media_twitter', 'social_media_instagram',
            'social_media_facebook', 'mem_location', 'mem_submitter')
        depth = 1


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'address', 'city', 'state', 'zipcode', 'time_active_start', 'time_active_end', 'lat_coord',
            'long_coord', 'permanent')


class MemorialMapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat_coord', 'long_coord', 'time_active_start', 'time_active_end')


class MemorialMapSerializer(serializers.ModelSerializer):
    mem_location = MemorialMapLocationSerializer(many=False)
    class Meta:
        model = Memorial
        fields = ('id', 'mem_location')
        depth = 1


class MemorialCreateSerializer(serializers.ModelSerializer):
    mem_location = LocationSerializer(many=False)
    mem_submitter = WebUserSerializer(many=False)

    class Meta:
        model = Memorial
        fields = (
            'id', 'name', 'memorial_day_observance', 'type', 'founder_name', 'email', 'profile_picture', 'google_virtual_tour',
            'website', 'description', 'memorial_type_desc', 'social_media_twitter', 'social_media_instagram',
            'social_media_facebook', 'mem_location', 'mem_submitter')

    def create(self, validated_data):
        location_data = validated_data.pop('mem_location')
        web_user_data = validated_data.pop('mem_submitter')

        mem_location_obj = Location.objects.create(**location_data)
        mem_submitter_obj = WebUser.objects.create(**web_user_data)

        memorial = Memorial.objects.create(mem_location=mem_location_obj,
                                           mem_submitter=mem_submitter_obj, **validated_data)
        return memorial


class MemorialUpdateSerializer(serializers.ModelSerializer):
    mem_location = LocationSerializer(many=False)
    mem_submitter = WebUserSerializer(many=False)

    class Meta:
        model = Memorial
        fields = (
            'id', 'name', 'memorial_day_observance', 'type', 'founder_name', 'email', 'profile_picture', 'google_virtual_tour',
            'website', 'description', 'memorial_type_desc', 'social_media_twitter', 'social_media_instagram',
            'social_media_facebook', 'mem_location', 'mem_submitter')

    def update(self, instance, validated_data):
        location_data = validated_data.pop('mem_location')
        web_user_data = validated_data.pop('mem_submitter')

        mem_location_obj, is_loc_updated = Location.objects.update_or_create(**location_data)
        mem_submitter_obj, is_sub_updated = WebUser.objects.update_or_create(**web_user_data)

        for mem in Memorial.objects.filter(id=instance.id):
            mem.name = validated_data.pop('name')
            mem.memorial_day_observance = validated_data.pop('memorial_day_observance')
            mem.type = validated_data.pop('type')
            mem.founder_name = validated_data.pop('founder_name')
            mem.email = validated_data.pop('email')
            mem.profile_picture = validated_data.pop('profile_picture')
            mem.google_virtual_tour = validated_data.pop('google_virtual_tour')
            mem.website = validated_data.pop('website')
            mem.description = validated_data.pop('description')
            mem.social_media_twitter = validated_data.pop('social_media_twitter')
            mem.social_media_instagram = validated_data.pop('social_media_instagram')
            mem.social_media_instagram = validated_data.pop('social_media_facebook')
            mem.memorial_type_desc = validated_data.pop('memorial_type_desc')
            mem.mem_location = mem_location_obj
            mem.mem_submitter = mem_submitter_obj
            mem.save()

        # memorial = Memorial.objects.filter(id=instance.id).update(mem_location=mem_location_obj,
        #                                                           mem_submitter=mem_submitter_obj, **validated_data)

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('first_name', 'last_name','inquiry','email', 'message')
        