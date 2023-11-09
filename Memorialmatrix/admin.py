from django.apps import AppConfig
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from Memorialmatrix.models import *
from django.contrib.auth.admin import UserAdmin
from Memorialmatrix.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import admin
from django.apps import apps


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode',)
    list_filter = ('email',)
    fieldsets = (
        (None,
         {'fields': ('email', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff', 'groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'address', 'city', 'state',
                'zipcode',)}
         ),
    )
    search_fields = ('email', 'address')
    ordering = ('email',)


class MemorialResource(resources.ModelResource):
    mem_location_id = fields.Field(
        column_name='mem_location',
        attribute='mem_location',
        widget=ForeignKeyWidget(Location, 'id'))

    mem_submitter_id = fields.Field(
        column_name='mem_submitter',
        attribute='mem_submitter',
        widget=ForeignKeyWidget(WebUser, 'id'))

    class Meta:
        model = Memorial
        fields = 'id', 'memorial_number', 'name', 'memorial_day_observance', 'memorial_type_desc', 'type', 'email', 'website', 'description', 'confirm_data_accuracy', \
                 'founder_name', 'is_approved', 'last_modified', 'social_media_twitter', 'social_media_facebook', 'social_media_instagram', \
                 'google_virtual_tour', 'mem_location_id', 'mem_submitter_id'

    def skip_row(self, instance, original):
        return True if Memorial.objects.filter(name=instance.name).exists() else False


class LocationResource(resources.ModelResource):
    class Meta:
        model = Location
        fields = 'id', 'location_number', 'type', 'address', 'city', 'state', 'zipcode', 'permanent', \
                 'time_active_start', 'time_active_end', 'lat_coord', 'long_coord', 'permanent', 'last_modified'

    def skip_row(self, instance, original):
        return True if Location.objects.filter(id=instance.id).exists() else False


class WebUserResource(resources.ModelResource):
    class Meta:
        model = WebUser
        fields = 'id', 'webuser_number', 'first_name', 'last_name', 'email', 'zipcode', 'web_user_loss', 'email_updates', 'created_date'


class MediaLinksResource(resources.ModelResource):
    mem_medialinks_id = fields.Field(
        column_name='mem_medialinks',
        attribute='mem_medialinks',
        widget=ForeignKeyWidget(Memorial, 'id'))

    class Meta:
        model = MediaLinks
        fields = 'id', 'medialinks_number', 'type', 'url', 'last_modified', 'mem_medialinks'

    def skip_row(self, instance, original):
        return True if MediaLinks.objects.filter(id=instance.id).exists() else False


class MediaLinksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MediaLinksResource
    list_display = ['mem_medialinks', 'id', 'medialinks_number', 'type', 'url']
    list_filter = ['id', 'type', 'url', 'mem_medialinks']
    exclude = ['medialinks_approval']


def approve_memorial(modeladmin, request, queryset):
    queryset.update(is_approved='approved')


approve_memorial.short_description = "Approve Selected Memorials"


def pending_memorial(modeladmin, request, queryset):
    queryset.update(is_approved='pending')


pending_memorial.short_description = "Set Pending Selected Memorials"


def disapprove_memorial(modeladmin, request, queryset):
    queryset.update(is_approved='disapproved')


disapprove_memorial.short_description = "Disapprove Selected Memorials"


class AdminApprovalQueueFilter(admin.SimpleListFilter):
    title = 'Admin Approval Queue'
    parameter_name = 'admin_approval_queue'

    def lookups(self, request, model_admin):
        return (
            ('pending', 'Pending'),
            ('not pending', 'Not Pending'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'pending' or value == 'Pending':
            return queryset.filter(is_approved='pending').order_by('last_modified')
        elif value == 'not pending' or value == 'Not Pending':
            return queryset.exclude(is_approved='pending').order_by('last_modified')
        return queryset


class MemorialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MemorialResource
    list_display = ['id', 'memorial_number', 'name','memorial_day_observance', 'type', 'email', 'website', 'description', 'confirm_data_accuracy',
                    'founder_name', 'is_approved', 'last_modified',
                    'social_media_twitter', 'social_media_facebook', 'social_media_instagram', 'google_virtual_tour',
                    'memorial_type_desc', 'mem_location_id',
                    'mem_submitter_id']
    list_filter = [AdminApprovalQueueFilter, 'name', 'type', 'email', 'is_approved', 'founder_name', 'last_modified']
    search_fields = ['id', 'name', 'type', 'founder_name', 'website']
    actions = [approve_memorial, pending_memorial, disapprove_memorial]

class LocationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LocationResource
    list_display = ['id', 'location_number', 'type', 'address', 'city', 'state', 'zipcode', 'time_active_start',
                    'time_active_end',
                    'lat_coord', 'long_coord', 'permanent', 'last_modified']
    list_filter = ['type', 'address', 'city', 'state', 'zipcode', 'time_active_start', 'time_active_end', 'lat_coord',
                   'long_coord', 'permanent']
    search_fields = ['id', 'type', 'city', 'state', 'zipcode', 'time_active_start', 'time_active_end']
    exclude = ['location_approval']


class WebUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = WebUserResource
    list_display = ['id', 'webuser_number', 'first_name', 'last_name', 'email', 'zipcode', 'web_user_loss',
                    'web_user_affiliated',
                    'email_updates',
                    'created_date']
    list_filter = ['first_name', 'last_name', 'email', 'zipcode', 'web_user_loss', 'web_user_affiliated', 'email_updates']
    search_fields = ['id', 'first_name', 'last_name', 'email', 'zipcode']


class History_MemorialAdmin(admin.ModelAdmin):
    list_display = ['id', 'memorial_number', 'name', 'memorial_day_observance', 'type', 'email', 'website', 'description', 'confirm_data_accuracy',
                    'founder_name', 'is_approved', 'history_date', 'history_type',
                    'social_media_twitter', 'social_media_facebook', 'social_media_instagram', 'google_virtual_tour',
                    'memorial_type_desc', 'mem_location_id',
                    'mem_submitter_id']
    list_filter = ['name', 'memorial_day_observance', 'type', 'email', 'is_approved', 'founder_name', 'last_modified']
    search_fields = ['id', 'name', 'type', 'founder_name', 'website']

    def queryset(self, request, queryset):
        model = Memorial.history.model

        return model.objects.raw('SELECT * FROM History_Memorial')


class History_LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_number', 'type', 'address', 'city', 'state', 'zipcode', 'time_active_start',
                    'time_active_end',
                    'lat_coord', 'long_coord', 'permanent', 'history_date', 'history_type', 'last_modified']
    list_filter = ['type', 'address', 'city', 'state', 'zipcode', 'time_active_start', 'time_active_end', 'lat_coord',
                   'long_coord', 'permanent']
    search_fields = ['id', 'type', 'city', 'state', 'zipcode', 'time_active_start', 'time_active_end']

    def queryset(self, request, queryset):
        model = Location.history.model
        return model.objects.raw('SELECT * FROM History_Location')


class History_WebUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'webuser_number', 'first_name', 'last_name', 'email', 'zipcode', 'history_date',
                    'history_type']
    list_filter = ['first_name', 'last_name', 'email', 'zipcode']
    search_fields = ['id', 'first_name', 'last_name', 'email', 'zipcode']

    def queryset(self, request, queryset):
        model = WebUser.history.model
        return model.objects.raw('SELECT * FROM History_WebUser')


class History_MediaLinksAdmin(admin.ModelAdmin):
    list_display = ['mem_medialinks', 'id', 'medialinks_number', 'type', 'url', 'history_date', 'history_type', ]
    list_filter = ['type', 'url']
    search_fields = ['id', 'type', 'url', 'mem_medialinks']

    def queryset(self, request, queryset):
        model = MediaLinks.history.model
        return model.objects.raw('SELECT * FROM History_MediaLinks')


class History_CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser.history.model
    list_display = ['email', 'first_name', 'last_name', 'phone', 'address', 'city', 'state', 'zipcode', 'history_date',
                    'history_type']
    list_filter = ['email']

    def queryset(self, request, queryset):
        model = CustomUser.history.model
        return model.objects.raw('SELECT * FROM History_CustomUser')
    

class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['first_name', 'last_name', 'inquiry', 'email', 'message', 'is_read', 'notes', 'message_received_date']
    list_fields = ['first_name', 'last_name', 'inquiry', 'email', 'message', 'is_read', 'notes', 'message_received_date']
    search_fields = ['first_name', 'last_name', 'inquiry', 'email', 'message', 'is_read', 'notes', 'message_received_date']

class WebsiteConfigParameterAdmin(admin.ModelAdmin):
    model = WebsiteConfigParameter
    list_display = ['parameter_name', 'parameter_value', 'is_enabled', 'parameter_description', 'created_date', 'last_updated_date']
    list_fields = ['parameter_name', 'parameter_value', 'created_date', 'last_updated_date']
    search_fields = ['parameter_name', 'parameter_value']


admin.site.register(Memorial.history.model, History_MemorialAdmin)
admin.site.register(CustomUser.history.model, History_CustomUserAdmin)
admin.site.register(Location.history.model, History_LocationAdmin)
admin.site.register(WebUser.history.model, History_WebUserAdmin)
admin.site.register(MediaLinks.history.model, History_MediaLinksAdmin)
admin.site.register(Memorial, MemorialAdmin)
admin.site.register(WebUser, WebUserAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MediaLinks, MediaLinksAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(WebsiteConfigParameter, WebsiteConfigParameterAdmin)

for model in AppConfig.get_models(apps.get_app_config('Memorialmatrix'), include_auto_created=False):
    try:
        admin.site.register(model)

    except admin.sites.AlreadyRegistered:
        pass