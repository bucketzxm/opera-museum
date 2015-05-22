# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'\xe8\xaf\x8d\xe6\x9d\xa1Id', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe8\xaf\x8d\xe6\x9d\xa1\xe5\x90\x8d\xe7\xa7\xb0')),
                ('content', models.TextField(verbose_name=b'\xe8\xaf\x8d\xe6\x9d\xa1\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('video_url', models.TextField(verbose_name=b'\xe8\xa7\x86\xe5\xb1\x8f\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('support', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0\xe9\x87\x8f')),
                ('watched', models.IntegerField(default=0, verbose_name=b'\xe8\xa7\x82\xe7\x9c\x8b\xe6\x95\xb0\xe9\x87\x8f')),
                ('relate_entry', models.ManyToManyField(related_name='relate_entry_rel_+', verbose_name=b'\xe7\x9b\xb8\xe5\x85\xb3\xe8\xaf\x8d\xe6\x9d\xa1', to='museum.Entry', blank=True)),
            ],
            options={
                'verbose_name': '\u8bcd\u6761',
                'verbose_name_plural': '\u8bcd\u6761',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_url', models.ImageField(upload_to=b'EntryImages/%Y/%m/%d', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe5\x9c\xb0\xe5\x9d\x80')),
                ('description', models.TextField(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('entry', models.ForeignKey(verbose_name=b'\xe5\xaf\xb9\xe5\xba\x94\xe8\xaf\x8d\xe6\x9d\xa1', blank=True, to='museum.Entry', null=True)),
            ],
            options={
                'verbose_name': '\u56fe\u7247',
                'verbose_name_plural': '\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=256, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x90\x8d\xe5\xad\x97')),
                ('value', models.CharField(max_length=256, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x86\x85\xe5\xae\xb9')),
                ('father', models.ForeignKey(related_name='fTag', default=b'', blank=True, to='museum.Tag', null=True, verbose_name=b'\xe7\x88\xb6\xe4\xba\xb2\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u5c5e\u6027',
                'verbose_name_plural': '\u5c5e\u6027',
            },
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='museum.Tag', verbose_name='\u5c5e\u6027\u5206\u7c7b', blank=True),
        ),
    ]
