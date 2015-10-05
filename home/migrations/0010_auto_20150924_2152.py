# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150922_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(max_length=100), icon='list-ul')), ('bio', wagtail.wagtailcore.blocks.StructBlock([(b'avatar', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'name', wagtail.wagtailcore.blocks.TextBlock()), (b'bio', wagtail.wagtailcore.blocks.RichTextBlock())])), ('bust_out', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.TextBlock()), (b'inverted', wagtail.wagtailcore.blocks.BooleanBlock(default=False))])), ('bust_out_quote', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'quote', wagtail.wagtailcore.blocks.TextBlock()), (b'source', wagtail.wagtailcore.blocks.TextBlock()), (b'inverted', wagtail.wagtailcore.blocks.BooleanBlock(default=False))]))]),
        ),
    ]
