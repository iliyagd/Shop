from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from .forms import SearchForm

from .models import product
from .models import Category

class products(ListView):
    model = product
    template_name = 'product.html'
    context_object_name = 'products'

class Category(ListView):
    template_name = 'Category.html'
    model = Category
    context_object_name = 'Categorys'
    
    
class ProductsDetail(DetailView):
    template_name = 'productView.html'
    model = product
    context_object_name = 'products'
    slug_field = 'ProductName'



    




