# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20150928_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualPromoteHeader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(max_length=200)),
                ('site_subtitle', models.CharField(max_length=200)),
                ('user_bio', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.UserBio', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='user_bio',
        ),
        migrations.AddField(
            model_name='homepage',
            name='page_header',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='home.IndividualPromoteHeader', null=True),
        ),
    ]
