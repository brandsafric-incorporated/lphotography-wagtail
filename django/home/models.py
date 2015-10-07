from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.models import Image, AbstractImage, AbstractRendition
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch import index

import struct
from PIL import Image as PILImage
from numpy import array, amin
from scipy.cluster.vq import kmeans2


class SmartImage(AbstractImage):
    dominant_foreground_color = models.CharField(max_length=6, blank=True)
    dominant_midground_color = models.CharField(max_length=6, blank=True)
    dominant_background_color = models.CharField(max_length=6, blank=True)

    admin_form_fields = Image.admin_form_fields + ('dominant_foreground_color', 'dominant_background_color', 'dominant_midground_color')

    def save(self, update_fields=None, *args, **kwargs):
        adding = self._state.adding
        super(AbstractImage, self).save(*args, **kwargs)
        if adding or (update_fields and 'image' in update_fields):
            img = PILImage.open(self.file.path)
            img_data = array(img.getdata()).astype(float)

            min_color_value = amin(img_data)

            centroids, _ = kmeans2(img_data, 3, iter=20)
            dominant_colors = sorted(centroids.astype(int).tolist())

            bg, mg, fg = [struct.pack('BBB', *rgb_value).encode('hex') for rgb_value in dominant_colors]

            self.dominant_foreground_color = fg
            self.dominant_midground_color = mg
            self.dominant_background_color = bg
            self.save()


class SmartImageRendition(AbstractRendition):
    image = models.ForeignKey(SmartImage, related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter', 'focal_point_key'),
        )


# Delete the source image file when an image is deleted
@receiver(pre_delete, sender=SmartImage)
def image_delete(sender, instance, **kwargs):
    instance.file.delete(False)


# Delete the rendition image file when a rendition is deleted
@receiver(pre_delete, sender=SmartImageRendition)
def rendition_delete(sender, instance, **kwargs):
    instance.file.delete(False)


class ImagePairBlock(blocks.StructBlock):
    image_one = ImageChooserBlock()
    image_two = ImageChooserBlock()

    class Meta:
        icon = 'image'
        template = 'home/image_pair_block.html'


class ImageTriadBlock(blocks.StructBlock):
    image_one = ImageChooserBlock()
    image_two = ImageChooserBlock()
    image_three = ImageChooserBlock()

    class Meta:
        icon = 'image'
        template = 'home/image_triad_block.html'


class BustOutBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()
    inverted = blocks.BooleanBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/bust_out_block.html'


class BustOutQuoteBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    quote = blocks.TextBlock()
    source = blocks.TextBlock()
    inverted = blocks.BooleanBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'home/bust_out_quote_block.html'


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(max_length=30)
    page_link = blocks.PageChooserBlock()
    button_type = blocks.ChoiceBlock(choices=[
        ('default', 'Default'),
        ('primary', 'Primary'),
        ('success', 'Success'),
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('danger', 'Danger'),
        ('link', 'Link'),
    ])

    class Meta:
        icon = 'radio-full'
        template = 'home/button.html'


@register_snippet
class UserBio(models.Model):
    avatar = models.ForeignKey('SmartImage', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(max_length=200)
    bio = RichTextField()

    panels = [
        FieldPanel('avatar'),
        FieldPanel('name'),
        FieldPanel('bio'),
    ]

    def __unicode__(self):
        return self.name


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
    background_image = models.ForeignKey('SmartImage', null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='+')
    page_header = models.ForeignKey('IndividualPromoteHeader', null=True, blank=True, on_delete=models.SET_NULL,
                                    related_name='+')

    content_panels = Page.content_panels + [
        FieldPanel('long_title', classname='full'),
        ImageChooserPanel('background_image'),
        SnippetChooserPanel('page_header'),
        StreamFieldPanel('body'),
    ]


@register_snippet
class IndividualPromoteHeader(models.Model):
    site_title = models.CharField(max_length=200)
    site_subtitle = models.CharField(max_length=200)
    user_bio = models.ForeignKey('UserBio', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel('site_title'),
        FieldPanel('site_subtitle'),
        FieldPanel('user_bio'),
    ]

    def __unicode__(self):
        return self.site_title + ' - ' + unicode(self.user_bio)
