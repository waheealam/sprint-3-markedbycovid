"""markedbycovid URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import report_builder
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import include, url
from Memorialmatrix import views
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.urls import path
from .api import api_router

admin.site.site_header = 'Memorial Matrix Administration Portal'
admin.site.site_title = 'Marked By Covid Admin'
admin.site.index_title = 'Marked By Covid'


urlpatterns = [
                  path('grappelli/', include('grappelli.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('Memorialmatrix.urls')),
                  path('report_builder/', include('report_builder.urls')),
                  # for wagtail
                  path('api/v2/', api_router.urls),
                  path('cms/', include(wagtailadmin_urls)),
                  path('documents/', include(wagtaildocs_urls)),
                  path('pages/', include(wagtail_urls)),
                  url(r'^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
                  path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),

              ]