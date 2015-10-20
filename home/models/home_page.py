from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from .blocks import ImagePairBlock, ImageTriadBlock, BustOutBlock, BustOutQuoteBlock, ButtonBlock
from .smart_image import SmartImage
from .snippets import IndividualPromoteHeader


class HomePage(Page):
    long_title = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="A longer, more verbose title that will be displayed on the page body")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", icon='title', template='home/heading.html')),
        ('content', blocks.RichTextBlock(icon='pilcrow', template='home/paragraph.html')),
        ('image', ImageChooserBlock(icon='image')),
        ('image_pair', ImagePairBlock()),
        ('image_triad', ImageTriadBlock()),
        ('list', blocks.ListBlock(blocks.CharBlock(max_length=100), icon='list-ul')),
        ('bust_out', BustOutBlock()),
        ('bust_out_quote', BustOutQuoteBlock()),
        ('button', ButtonBlock()),
    ])
    background_image = models.ForeignKey(SmartImage, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='+')
    page_header = models.ForeignKey(IndividualPromoteHeader, null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('long_title', classname='full'),
        ImageChooserPanel('background_image'),
        SnippetChooserPanel('page_header'),
        StreamFieldPanel('body'),
    ]
