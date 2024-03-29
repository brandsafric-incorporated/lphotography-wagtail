# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailadmin.taggable
import wagtail.wagtailimages.blocks
import wagtail.wagtailimages.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.wagtailimages.models.get_upload_to, width_field='width', verbose_name='File')),
                ('width', models.IntegerField(verbose_name='Width', editable=False)),
                ('height', models.IntegerField(verbose_name='Height', editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at', db_index=True)),
                ('focal_point_x', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_y', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_width', models.PositiveIntegerField(null=True, blank=True)),
                ('focal_point_height', models.PositiveIntegerField(null=True, blank=True)),
                ('file_size', models.PositiveIntegerField(null=True, editable=False)),
                ('dominant_foreground_color', models.CharField(max_length=6, blank=True)),
                ('dominant_background_color', models.CharField(max_length=6, blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='Tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
        migrations.CreateModel(
            name='SmartImageRendition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(height_field='height', width_field='width', upload_to='images')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(default='', max_length=255, editable=False, blank=True)),
                ('filter', models.ForeignKey(related_name='+', to='wagtailimages.Filter')),
                ('image', models.ForeignKey(related_name='renditions', to='home.SmartImage')),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailcore.blocks.RichTextBlock()), ('list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(max_length=100))), ('bust_out', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'text', wagtail.wagtailcore.blocks.TextBlock())]))], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='background_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.SmartImage', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='smartimagerendition',
            unique_together=set([('image', 'filter', 'focal_point_key')]),
        ),
    ]
