# -*- coding: utf-8 -*-
"""
admin.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.contrib import admin
from catalogo.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']
    search_fields = ('id','title')
    list_filter = ('id','title')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']
    list_filter = ('id','title')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
