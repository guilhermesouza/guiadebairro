# -*- coding: utf-8 -*-
"""
admin.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.contrib import admin
from anuncio.models import Anuncio, Categoria

class AnuncioAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ['titulo']
    search_fields = ('id','titulo')
    list_filter = ('id','titulo')

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ['titulo']
    list_filter = ('id','titulo')


admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Categoria, CategoriaAdmin)
