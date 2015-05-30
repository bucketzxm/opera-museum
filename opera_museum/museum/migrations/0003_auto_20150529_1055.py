# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0002_entry_slider_show'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='support',
            new_name='like',
        ),
    ]
