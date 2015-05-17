#!-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Image(models.Model):
    image_url = models.FileField(verbose_name="图片地址")
    description = models.TextField(blank=True, verbose_name="图片描述")

    def __str__(self):
        return u'图片 %s' % self.description

    def __unicode__(self):
        return u'图片 %s' % self.description

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = "图片"

class Tag(models.Model):
    key = models.CharField(max_length=256, verbose_name="属性名字")
    value = models.CharField(max_length=256, verbose_name="属性内容")

    def __str__(self):
        return u'图片 %s' % self.description

    def __unicode__(self):
        return u'图片 %s' % self.description

    class Meta:
        verbose_name = "属性"
        verbose_name_plural = "属性"

class Entry(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="词条Id")
    name = models.CharField(max_length=128, verbose_name="词条名称")
    content = models.TextField(blank=True, verbose_name="词条内容")
    images = models.ManyToManyField(Image, blank=True, verbose_name="图片")
    video_url = models.TextField(blank=True, verbose_name="视屏链接")
    relate_entry = models.TextField(blank=True, verbose_name="相关词条")
    Tag = models.ManyToManyField(Tag, blank=True, verbose_name="属性分类")


    def __str__(self):
        return u'词条 %s : %s ' % ( str(self.id), self.name )

    def __unicode__(self):
        return u'词条 %s : %s ' % ( str(self.id), self.name )


    class Meta:
        verbose_name = "词条"
        verbose_name_plural = "词条"

