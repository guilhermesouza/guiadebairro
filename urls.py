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
from catalogo.models import *
from django.views.generic.list_detail import object_list
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'catalogo.views.index'),
#   url(r'^catalogo/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$', 'catalogo.views.view_post', name='view_catalogo_post'),
#    url(r'^catalogo/', object_list, {'queryset': Post.objects.all() }),
    
    #catalogo
    url(r'^catalogo/(?P<slug>[^\.]+)','catalogo.views.view_post',name='view_catalogo_post'),
    url(r'^catalogo/category/(?P<slug>[^\.]+).html', 'catalogo.views.view_category', name='view_catalogo_category'),


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
