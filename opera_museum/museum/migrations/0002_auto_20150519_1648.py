# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.FileField(upload_to=b'EntryImages/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
