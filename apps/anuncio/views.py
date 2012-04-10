# -*- coding: utf-8 -*-
"""
views.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from anuncio.models import Anuncio, Categoria
from django.shortcuts import render_to_response, get_object_or_404


#exibe os anuncios
def index(request):
    return render_to_response('anuncio/index.html', {
    'categorias': Categoria.objects.all(),
    'anuncios': Anuncio.objects.all()
})

#exibe os anuncios
def view_anuncio(request, slug):
    return render_to_response('anuncio/view_anuncio.html', {
        'anuncio': get_object_or_404(Anuncio, slug=slug)
})

#exibe as categorias
def view_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render_to_response('anuncio/view_categoria.html', {
        'categoria': categoria,
        'anuncios': Anuncio.objects.filter(categoria=categoria)
})

#exibe a lista de categorias
def catalogo(request):
    return render_to_response('anuncio/catalogo.html', {
    #'categorias': Categoria.objects.all(),
    'categorias': Categoria.objects.order_by('titulo'),
    'anuncios': Anuncio.objects.all()
})
