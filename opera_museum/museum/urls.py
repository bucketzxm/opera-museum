__author__ = 'simon'

from django.conf.urls.static import static
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^rest/v1/index/indexImages/(?P<page>[0-9]+)$', views.indexData),
    url(r'^get_entry_json',views.get_entry_json),
    url(r'^get_slider_json',views.get_slider_json),
    url(r'^entry_detail', views.entry_detail),
    # url(r'^get_entry_detail_json', views.get_entry_detail_json),
    # url(r'^get_relate_entry_json', views.get_relate_entry_json),
    url(r'^like_entry', views.like_entry),

]
