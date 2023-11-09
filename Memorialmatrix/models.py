from __future__ import unicode_literals

import uuid

from crum import get_current_user
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.core.validators import *
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from Memorialmatrix.managers import CustomUserManager
from Memorialmatrix.validators import *


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_number = models.IntegerField(default=1, editable=False)
    email = models.EmailField(_('email address'), validators=[validate_email], unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=2, blank=True, validators=[MinLengthValidator(2)])
    zipcode = models.CharField(max_length=5, validators=[validate_integer, MinLengthValidator(5)], blank=True)
    phone = models.CharField(max_length=10, blank=True, validators=[MinLengthValidator(10)])
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} {str(self.admin_number)}'

    class Meta:
        verbose_name_plural = "Admins"
        verbose_name = "Admin"

    history = HistoricalRecords(cascade_delete_history=True, table_name="History_Admin",
                                verbose_name=" History_Admin", custom_model_name="History_Admin")


class WebUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    webuser_number = models.IntegerField(editable=False, default=1, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10, null=True)
    web_user_loss = models.BooleanField(default=False)
    web_user_affiliated = models.BooleanField(default=False)
    email_updates = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(cascade_delete_history=True, table_name="History_WebUser",
                                verbose_name=" History_WebUser",
                                custom_model_name="History_WebUser")

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        try:
            if self._state.adding:
                last_id = WebUser.objects.all().aggregate(largest=models.Max('webuser_number'))['largest']
                if last_id is not None:
                    self.webuser_number = last_id + 1
        except:
            pass
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user

        super(WebUser, self).save(*args, **kwargs)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_number = models.IntegerField(editable=False, default=1, blank=True)
    type = models.CharField(max_length=75, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=5, null=True, blank=True)
    time_active_start = models.DateField(null=True, blank=True)
    time_active_end = models.DateField(null=True, blank=True)
    lat_coord = models.DecimalField(max_digits=17, decimal_places=15, null=True,
                                    blank=True)
    long_coord = models.DecimalField(max_digits=18, decimal_places=15, null=True, blank=True)
    permanent_choices = (
        ('temporary', 'Temporary'), ('permanent', 'Permanent'))
    permanent = models.CharField(
        choices=permanent_choices, blank=True, null=True, max_length=9)
    location_approval = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(cascade_delete_history=True, table_name="History_Location",
                                verbose_name=" History_Location",
                                custom_model_name="History_Location")

    def save(self, *args, **kwargs):
        try:
            if self._state.adding:
                last_id = Location.objects.all().aggregate(largest=models.Max('location_number'))['largest']
                if last_id is not None:
                    self.location_number = last_id + 1
        except:
            pass
        user = get_current_user()
        str_user = str(user)
        if str_user == 'AnonymousUser':
            self.location_approval = False
        elif str_user != 'AnonymousUser':
            try:
                superuserPK = CustomUser.objects.get(email=user)
                returnSuperuser = superuserPK.is_superuser
                if not returnSuperuser:
                    self.location_approval = False
            except:
                pass
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user

        super(Location, self).save(*args, **kwargs)

    def __str__(self):
        return f'{str(self.location_number)}'


class Memorial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    memorial_number = models.IntegerField(editable=False, default=1, blank=True)
    mem_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='mem_location', blank=True,
                                     null=True)
    mem_submitter = models.ForeignKey(WebUser, on_delete=models.CASCADE, related_name='mem_submitter', blank=True,
                                      null=True)
    name = models.CharField(max_length=75)
    memorial_day_observance = models.BooleanField(default=False)
    type_choices = (('physical', 'Physical'), ('virtual', 'Virtual'))
    type = models.CharField(max_length=75, choices=type_choices, null=True, blank=True)
    profile_picture = models.URLField(max_length=200, null=True, blank=True)
    google_virtual_tour = models.URLField(max_length=200, null=True, blank=True)
    memorial_type_desc = models.CharField(max_length=75, null=True, blank=True)
    founder_name = models.CharField(max_length=75, null=True, blank=True)
    website = models.URLField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    confirm_data_accuracy = models.BooleanField(default=False)
    description = models.TextField(max_length=4096, null=True, blank=True)
    social_media_twitter = models.URLField(max_length=200, null=True, blank=True)
    social_media_facebook = models.URLField(max_length=200, null=True, blank=True)
    social_media_instagram = models.URLField(max_length=200, null=True, blank=True)
    is_approved_choices = (
        ('pending', 'Pending'), ('disapproved', 'Disapproved'), ('approved', 'Approved'))
    is_approved = models.CharField(
        choices=is_approved_choices, max_length=11, default='Pending')
    is_featured = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(cascade_delete_history=True, table_name="History_Memorial",
                                verbose_name=" History_Memorial",
                                custom_model_name="History_Memorial")

    def __str__(self):
        return f'{self.name} {str(self.memorial_number)}'

    def save(self, *args, **kwargs):
        try:
            if self._state.adding:
                last_id = Memorial.objects.all().aggregate(largest=models.Max('memorial_number'))['largest']
                if last_id is not None:
                    self.memorial_number = last_id + 1
        except:
            pass
        user = get_current_user()
        str_user = str(user)
        if str_user == 'AnonymousUser':
            self.is_approved = 'pending'
        elif str_user != 'AnonymousUser':
            try:
                superuserPK = CustomUser.objects.get(email=user)
                returnSuperuser = superuserPK.is_superuser
                if not returnSuperuser:
                    self.is_approved = 'pending'
            except:
                pass
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user

        super(Memorial, self).save(*args, **kwargs)


class MediaLinks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medialinks_number = models.IntegerField(default=1, editable=False)
    mem_medialinks = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='mem_medialinks', blank=True,
                                       null=True)
    type_choices = (('photo', 'Photo'), ('video', 'Video'),
                    ('press coverage', 'Press Coverage'))
    type = models.CharField(max_length=75, choices=type_choices)
    url = models.URLField(max_length=200)
    medialinks_approval = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(cascade_delete_history=True, table_name="History_MediaLinks",
                                verbose_name=" History_MediaLink",
                                custom_model_name="History_MediaLinks")

    class Meta:
        verbose_name_plural = "MediaLinks"
        verbose_name = "MediaLinks"

    def __str__(self):
        return f'{str(self.medialinks_number)}'

    def save(self, *args, **kwargs):
        try:
            if self._state.adding:
                last_id = MediaLinks.objects.all().aggregate(largest=models.Max('medialinks_number'))['largest']
                if last_id is not None:
                    self.medialinks_number = last_id + 1
        except:
            pass
        user = get_current_user()
        str_user = str(user)
        if str_user == 'AnonymousUser':
            self.is_approved = 'pending'
        elif str_user != 'AnonymousUser':
            try:
                superuserPK = CustomUser.objects.get(email=user)
                returnSuperuser = superuserPK.is_superuser
                if not returnSuperuser:
                    self.medialinks_approval = False
            except:
                pass
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(MediaLinks, self).save(*args, **kwargs)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    inquiry = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.TextField(max_length=4096, null=False)
    is_read = models.BooleanField(default=False)
    notes = models.CharField(max_length=250, null=True, blank=True)
    message_received_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.email


class WebsiteConfigParameter(models.Model):
    parameter_name = models.CharField(primary_key=True, max_length=50, null=False)
    parameter_value = models.TextField(null=False)
    parameter_description = models.TextField(null=False, default='')
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.parameter_name, self.parameter_value)
