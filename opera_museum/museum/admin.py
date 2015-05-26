# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.contrib import admin

# Register your models here.

from models import Entry, Tag, Image
from kombu.transport.django import models as kombu_models

# Here we do some operatino before change entry in the admin site

def delete_relate_entry(me, other):
    me.relate_entry.remove(other)
    print("Before we save the Entry")
    other.relate_entry.remove(me)


def add_relate_entry(me, other):
    me.relate_entry.add(other)
    other.relate_entry.add(me)


def do_with_entry(entry, operate):
    for r_entry in entry.relate_entry:
        operate(entry, r_entry)



from museum.tasks import add_related_entries, delete_relate_entries

class EntryAdmin(admin.ModelAdmin):
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
