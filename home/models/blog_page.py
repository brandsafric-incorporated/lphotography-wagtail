from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from .smart_image import SmartImage


class BlogPage(Page):
    image = models.ForeignKey(SmartImage, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('body', classname='full'),
    ]
