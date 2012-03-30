# -*- coding: utf-8 -*-
"""
views.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from catalogo.models import Anuncios, Categorias
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('catalogo/index.html', {
    'categorias': Categorias.objects.all(),
    'anuncios': Anuncios.objects.all()[:5]
})

def view_anuncios(request, slug):
    return render_to_response('catalogo/view_anuncio.html', {
        'anuncio': get_object_or_404(Anuncios, slug=slug)
})

def view_categorias(request, slug):
    categoria = get_object_or_404(Categorias, slug=slug)
    return render_to_response('catalogo/view_categoria.html', {
        'categorias': categoria,
        'anuncios': Anuncios.objects.filter(categorias=categoria)[:5]
})

