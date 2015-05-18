# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='relate_entry',
        ),
        migrations.AddField(
            model_name='entry',
            name='relate_entry',
            field=models.ManyToManyField(related_name='relate_entry_rel_+', verbose_name=b'\xe7\x9b\xb8\xe5\x85\xb3\xe8\xaf\x8d\xe6\x9d\xa1', to='museum.Entry', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.FileField(upload_to=b'EntryImages/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
    ]
