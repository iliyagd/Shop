from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import product , Category


class Blog(ListView):
    template_name = 'blog.html'
    model = product
    context_object_name = 'products'

class Category(ListView):
    template_name = 'Category.html'
    model = Category
    context_object_name = 'Categorys'    


class BlogDetail(DetailView):
    template_name = 'Products.html'
    model = product
    context_object_name = 'products'
    slug_field = 'ProductName'
