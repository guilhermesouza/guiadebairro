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

class Anuncio(models.Model):
    titulo = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField()
    categoria = models.ForeignKey('anuncio.Categoria')
    publicado = models.DateTimeField(auto_now_add=True)
    #photo = ImageWithThumbsField(null=True, blank=True, upload_to='galeria', sizes=((90,90),(200,100)))
    #thumbnail = ImageWithThumbsField(null=True, blank=True, upload_to='galeria/thumbnail')
    foto = models.ImageField(null=True, blank = True, upload_to='anuncios/')
    
    def __unicode__(self):
        return self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_anuncio_anuncio', None, { 'slug': self.slug })
    class Meta:
        verbose_name_plural = 'Anuncios'

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_absolute_url(self):
        return ('view_anuncio_categoria', None, { 'slug': self.slug })

    class Meta:
        verbose_name_plural = 'Categorias'

