from django.contrib import admin

# Register your models here.

from models import Entry, Tag, Image
from kombu.transport.django import models as kombu_models

admin.site.register(Entry)
admin.site.register(Image)
admin.site.register(Tag)

admin.site.register(kombu_models.Message)


