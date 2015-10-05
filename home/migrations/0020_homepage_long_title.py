# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_smartimage_dominant_midground_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='long_title',
            field=models.CharField(help_text='A longer, more verbose title that will be displayed on the page body', max_length=255, null=True, blank=True),
        ),
    ]
