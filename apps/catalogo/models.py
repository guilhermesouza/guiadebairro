# -*- coding: utf-8 -*-
"""
models.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""
#http://www.djangorocks.com/tutorials/how-to-create-a-basic-blog-in-django/defining-your-models.html
#http://vimeo.com/14884657

from django.db import models
from django.db.models import permalink
#from thumbs import ImageWithThumbsField

class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    category = models.ForeignKey('catalogo.Category')
    created = models.DateTimeField(auto_now_add=True)
    #photo = ImageWithThumbsField(null=True, blank=True, upload_to='galeria', sizes=((90,90),(200,100)))
    #thumbnail = ImageWithThumbsField(null=True, blank=True, upload_to='galeria/thumbnail')
    photo = models.ImageField(null=True, blank = True, upload_to='post/')
    
    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_catalogo_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_catalogo_category', None, { 'slug': self.slug })



