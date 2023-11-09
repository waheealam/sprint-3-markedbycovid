from django.urls import path
from . import views

urlpatterns = [
    # path('api/list/', views.memorialList, name="memorial-list"),
    path('api/detail/<str:pk>/', views.memorialDetail, name="memorial-detail"),
    path('api/memorial/list', views.memorial_list),
    path('api/memorial/count', views.memorial_approved_count),
    path('api/memorial/upcomingEvents', views.memorial_upcoming_events),
    path('api/memorial/featuredMemorials', views.memorial_featured_memorials),
    path('api/memorial/detail/<str:id>', views.memorial_detail_view),
    path('api/location/list/', views.location_list),
    path('api/create/', views.memorialCreate, name="memorial-create"),
    path('api/update/<str:pk>/', views.memorialUpdate, name="memorial-update"),
    path('api/mapMemorials', views.memorial_map_List),
    path('api/medialink/list/', views.medialink_list),
    path('api/medialink/<str:mem_id>', views.memorialMediaLinks),
    path('api/medialinkCreate/', views.medialinkCreateOrUpdate),
    path('api/medialinkUpdate/', views.medialinkCreateOrUpdate),
    path('api/contactus/', views.contactUs, name="contact-us"),
    path('api/memorial/profilePhoto/<str:mem_id>', views.memorial_profile_photo),
    path('api/website/configuration/parameter/<str:parameter_name>', views.website_configuration_parameter),
]
