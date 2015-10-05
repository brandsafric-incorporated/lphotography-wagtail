# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20150929_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('image_pair', wagtail.wagtailcore.blocks.StructBlock([(b'image_one', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'image_two', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('image_triad', wagtail.wagtailcore.blocks.StructBlock([(b'image_one', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'image_two', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'image_three', wagtail.wagtailimages.blocks.ImageChooserBlock())])), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(max_length=100), icon='list-ul')), ('bust_out', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.RichTextBlock()), (b'inverted', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])), ('bust_out_quote', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'quote', wagtail.wagtailcore.blocks.TextBlock()), (b'source', wagtail.wagtailcore.blocks.TextBlock()), (b'inverted', wagtail.wagtailcore.blocks.BooleanBlock(required=False))]))]),
        ),
    ]
