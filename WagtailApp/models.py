from django.db import models
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.models import Orderable


class CoreStaffDetail(blocks.StructBlock):
    staffName = CharBlock(max_length=255)
    staffDescription = RichTextBlock()
    photoUrl = blocks.URLBlock(max_length=2048, required=False)

class AboutPage(Page):
    pageTitle = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    coreStaffTitle = models.CharField(max_length=250, blank=True)
    coreStaffs = StreamField([
        ('coreStaffs', CoreStaffDetail()),
    ], default=[])

    content_panels = Page.content_panels + [
        FieldPanel('pageTitle'),
        FieldPanel('body', classname="full"),
        FieldPanel('coreStaffTitle'),
        StreamFieldPanel('coreStaffs')

    ]
    api_fields = [
        APIField('pageTitle'),
        APIField('body'),
        APIField('coreStaffTitle'),
        APIField('coreStaffs')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['corestaff_list'] = self.coreStaffs
        return context


class FooterPage(Page):

    donate = models.CharField(max_length=250, blank=True)
    facebookLink = models.CharField(max_length=250, blank=True)
    instagramLink = models.CharField(max_length=250, blank=True)
    twitterLink = models.CharField(max_length=250, blank=True)
    shareStoryLink = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('donate', classname="full"),
        FieldPanel('facebookLink', classname="full"),
        FieldPanel('instagramLink', classname="full"),
        FieldPanel('twitterLink', classname="full"),
        FieldPanel('shareStoryLink', classname="full"),
    ]
    api_fields = [
        APIField('donate'),
        APIField('facebookLink'),
        APIField('instagramLink'),
        APIField('twitterLink'),
        APIField('shareStoryLink'),
    ]


class FaqQuestion(blocks.StructBlock):
    question = CharBlock(max_length=255)
    answer = RichTextBlock()

    class Meta:
        icon = 'help'


class FaqPage(Page):
    questions = StreamField([
        ('faq_question', FaqQuestion()),
    ], default=[])

    content_panels = Page.content_panels + [
        StreamFieldPanel('questions')
    ]

    api_fields = [
        APIField('questions')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['faq_items'] = self.questions
        return context


class SponsorDetail(blocks.StructBlock):
    sponsorName = CharBlock(max_length=255)
    sponsorDescription = RichTextBlock()
    photoUrl = blocks.URLBlock(max_length=2048, required=False)

class AdvisorDetail(blocks.StructBlock):
    advisorName = CharBlock(max_length=255)
    advisorDescription = RichTextBlock()
    advisorPhotoUrl = blocks.URLBlock(max_length=2048, required=False)

class VolunteerDetail(blocks.StructBlock):
    volunteerName = CharBlock(max_length=255)
    volunteerDescription = RichTextBlock()
    volunteerPhotoUrl = blocks.URLBlock(max_length=2048, required=False)




class SponsorPage(Page):
    sponsors = StreamField([
        ('sponsor', SponsorDetail()),
    ], default=[])
    advisors = StreamField([
        ('advisors', AdvisorDetail()),
    ], default=[])
    volunteers = StreamField([
        ('volunteers', VolunteerDetail()),
    ], default=[])

    content_panels = Page.content_panels + [
        StreamFieldPanel('sponsors'),
        StreamFieldPanel('advisors'),
        StreamFieldPanel('volunteers')
    ]

    api_fields = [
        APIField('sponsors'),
        APIField('advisors'),
        APIField('volunteers')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['sponsor_list'] = self.sponsors
        return context