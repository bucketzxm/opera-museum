# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_auto_20150529_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='video_name',
            field=models.CharField(default=b'', max_length=60, verbose_name=b'\xe8\xa7\x86\xe5\xb1\x8f\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
