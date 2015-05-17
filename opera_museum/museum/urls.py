__author__ = 'simon'

from django.conf.urls.static import static
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),

]
