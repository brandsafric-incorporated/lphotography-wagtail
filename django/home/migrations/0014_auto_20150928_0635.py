# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20150927_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('bio', wagtail.wagtailcore.fields.RichTextField()),
                ('avatar', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.SmartImage', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='homepage',
            name='user_bio',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.UserBio', null=True),
        ),
    ]
