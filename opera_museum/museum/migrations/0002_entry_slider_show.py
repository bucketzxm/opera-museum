# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='slider_show',
            field=models.BooleanField(default=False, verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe8\xb7\x91\xe9\xa9\xac\xe7\x81\xaf\xe6\x98\xbe\xe7\xa4\xba'),
        ),
    ]
