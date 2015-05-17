from django.conf.urls import patterns, include, url
from django.contrib import admin
import museum.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opera_museum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(museum.urls)),
)
