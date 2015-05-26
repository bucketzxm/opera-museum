# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.contrib import admin

# Register your models here.

from models import Entry, Tag, Image
from kombu.transport.django import models as kombu_models

# Here we do some operatino before change entry in the admin site
from museum.tasks import add_related_entries, delete_relate_entries


class ImageInline(admin.TabularInline):
    model = Image

class EntryAdmin(admin.ModelAdmin):

    inlines = [
        ImageInline,
    ]

    def save_model(self, request, obj, form, change):
        obj.save()
        add_related_entries.delay(obj)

    def delete_model(self, request, obj):
        # obj.entry = request.entry
        delete_relate_entries.delay(obj)
        obj.delete()





admin.site.register(Entry, EntryAdmin)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(kombu_models.Message)
