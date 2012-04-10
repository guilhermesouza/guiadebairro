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
from anuncio.models import *
#from django.views.generic.list_detail import object_list
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    (r'^$', direct_to_template, {'template': 'index.html'}),

    (r'^anuncios/$', 'anuncio.views.index'),
    (r'^catalogo/$', 'anuncio.views.catalogo'),

#   url(r'^catalogo/', object_list, {'queryset': Anuncios.objects.all() }),
    
    # Anuncios / Categorias
    url(r'^anuncio/(?P<slug>[^\.]+)','anuncio.views.view_anuncio',name='view_anuncio_anuncio'),
    url(r'^categorias/(?P<slug>[^\.]+)', 'anuncio.views.view_categoria', name='view_anuncio_categoria'),

    # Media
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
