from django.contrib import admin

# Register your models here.

from models import Entry, Tag, Image


admin.site.register(Entry)
admin.site.register(Image)
admin.site.register(Tag)


