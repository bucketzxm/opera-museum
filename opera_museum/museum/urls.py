__author__ = 'simon'

from django.conf.urls.static import static
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^rest/v1/index/indexImages/(?P<page>[0-9]+)$', views.indexData),
    url(r'^get_entry_json',views.get_entry_json),
    url(r'^get_slider_json',views.get_slider_json),
]
