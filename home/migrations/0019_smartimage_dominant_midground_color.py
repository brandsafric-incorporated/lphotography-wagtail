# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20150929_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartimage',
            name='dominant_midground_color',
            field=models.CharField(max_length=6, blank=True),
        ),
    ]
