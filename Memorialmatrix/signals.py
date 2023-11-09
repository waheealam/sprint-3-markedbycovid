import os

from Memorialmatrix.models import *
# import Group models
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.signals import *
from report_builder.models import *
from liquid import Template
import time



@receiver(post_save, sender=Memorial)
def memorial_approval_signal(sender, instance, created, **kwargs):
    try:
        global message
        if instance.is_approved == 'approved':
            parameter = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_MESSAGE_MEMORIAL_APPROVED')
            if parameter.exists():
                message = parameter.get().parameter_value
            mem_location = Location.objects.filter(id=instance.mem_location.id)
            mem_location.update(location_approval=True)
            mem_medialinks = MediaLinks.objects.filter(mem_medialinks=instance.id)
            mem_medialinks.update(medialinks_approval=True)
            from_email = os.environ.get('EMAIL_HOST')
            to_email = instance.mem_submitter.email
            subject = f'Memorial Approved'
            template = Template(message)
            final_message = template.render(submitter_name=instance.mem_submitter.first_name, memorial_name=instance.name)
            send_mail(subject, final_message, from_email=from_email, recipient_list=[to_email])
        elif instance.is_approved == 'disapproved' or instance.is_approved == 'pending':
            parameter = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_MESSAGE_MEMORIAL_DISAPPROVAL')
            if parameter.exists():
                message = parameter.get().parameter_value
            mem_location = Location.objects.filter(id=instance.mem_location.id)
            mem_location.update(location_approval=False)
            mem_medialinks = MediaLinks.objects.filter(mem_medialinks=instance.id)
            mem_medialinks.update(medialinks_approval=False)
            from_email = os.environ.get('EMAIL_HOST')
            to_email = instance.mem_submitter.email
            subject = f'Memorial Not Approved'
            template = Template(message)
            final_message = template.render(submitter_name=instance.mem_submitter.first_name,
                                            memorial_name=instance.name)
            send_mail(subject, final_message, from_email=from_email, recipient_list=[to_email])
    except:
        pass


post_save.connect(memorial_approval_signal, sender=Memorial)


@receiver(post_save, sender=Location)
def location_approval_signal(sender, instance, created, **kwargs):
    try:
        location = Location.objects.filter(id=instance.id)
        memorial_for_location = Memorial.objects.filter(mem_location=instance.id)
        memorial = Memorial.objects.get(mem_location=instance.id)

        if instance.location_approval == 0:
            memorial_for_location.update(is_approved='pending')
        elif memorial.is_approved == 'approved':
            location.update(location_approval=True)

    except:
        pass


post_save.connect(location_approval_signal, sender=Location)

one_time_wait = 0


@receiver(post_save, sender=MediaLinks)
def medialinks_approval_signal(sender, instance, created, **kwargs):
    global one_time_wait
    try:
        if one_time_wait == 0:
            time.sleep(1.50)
            one_time_wait = 1
        medialinks = MediaLinks.objects.filter(id=instance.id)
        memorial_for_medialinks = Memorial.objects.filter(mem_medialinks=instance.id)
        memorial = Memorial.objects.get(mem_medialinks=instance.id)

        if instance.medialinks_approval == 0:
            memorial_for_medialinks.update(is_approved='pending')
        elif memorial.is_approved == 'approved':
            medialinks.update(medialinks_approval=True)
    except:
        pass


post_save.connect(location_approval_signal, sender=MediaLinks)


@receiver(post_save, sender=CustomUser)
def customuser_create_signal(sender, instance, created, **kwargs):
    try:
        if created:
            parameter = WebsiteConfigParameter.objects.filter(parameter_name='EMAIL_MESSAGE_NEW_USER')
            if parameter.exists():
                message = parameter.get().parameter_value
            first_name = instance.first_name
            from_email = os.environ.get('EMAIL_HOST')
            to_email = instance.email
            template = Template(message)
            final_message = template.render(user_first_name=first_name,
                                            user_email=instance.email)
            subject = f'Welcome Aboard'
            send_mail(subject, final_message, from_email=from_email, recipient_list=[to_email])
    except:
        pass
