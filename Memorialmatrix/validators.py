from urllib.parse import urlparse
from django.core.exceptions import ValidationError



def validate_twitter_url(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ('twitter.com'):
        raise ValidationError('Please Enter A Valid Twitter Link')


def validate_instagram_url(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ('instagram.com'):
        raise ValidationError('Please Enter A Valid Instagram Link')


def validate_facebook_url(value):
    if not value:
        return
    obj = urlparse(value)
    if not obj.hostname in ('facebook.com'):
        raise ValidationError('Please Enter A Valid Facebook Link')


def validate_date(value):
    value_time = int(value.strftime("%Y"))
    if value_time < 2020 or value_time > 2035:
        raise ValidationError(u'%s is not a valid year. Please use dates after 2019.' % value_time)
