# -*- coding: utf-8 -*-
"""
urls.py

Created by _Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.conf import settings
from meublog.blog.models import *
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meublog.views.home', name='home'),
    # url(r'^meublog/', include('meublog.foo.urls')),
    # Uncomment the next line to enable the admin:
    #url(r'^blog/', include(meublog.blog.urls)),

    url(r'^admin/', include(admin.site.urls)),


    (r'^$', 'meublog.blog.views.index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', 'meublog.blog.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', 'meublog.blog.views.view_category', name='view_blog_category'),


    (r'^media/(.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns( '',
        ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True} ),
)

if settings.DEBUG:
    urlpatterns += patterns( '',
        ( r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT} ),
)


# staticfiles
urlpatterns += staticfiles_urlpatterns()
