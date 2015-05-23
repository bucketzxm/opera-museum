from django.conf.urls import patterns, include, url
from django.contrib import admin

import museum.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opera_museum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'media/'}),
    url(r'', include(museum.urls)),
)
