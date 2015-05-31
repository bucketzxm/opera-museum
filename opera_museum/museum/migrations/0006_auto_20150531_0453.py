# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0005_entry_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='video_description',
            field=models.CharField(default=b'', max_length=60, verbose_name=b'\xe8\xa7\x86\xe5\xb1\x8f\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='video_name',
            field=models.CharField(default=b'', max_length=60, verbose_name=b'\xe8\xa7\x86\xe5\xb1\x8f\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
