# -*- coding: utf-8 -*-
"""
views.py

Created by Guilherme Souza on 2012-02-12.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from catalogo.models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    return render_to_response('catalogo/index.html', {
    'categories': Category.objects.all(),
    'posts': Post.objects.all()[:5]
})

def view_post(request, slug):
    return render_to_response('catalogo/view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('catalogo/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
})

