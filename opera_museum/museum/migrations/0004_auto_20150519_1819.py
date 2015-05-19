# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='support',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AddField(
            model_name='entry',
            name='watched',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xa7\x82\xe7\x9c\x8b\xe6\x95\xb0\xe9\x87\x8f'),
        ),
    ]
