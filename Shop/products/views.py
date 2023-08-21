from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import product

class products(ListView):
    template_name = 'product.html'
    model = product
    context_object_name = 'products'



class ProductsDetail(DetailView):
    template_name = 'productView.html'
    model = product
    context_object_name = 'products'
    slug_field = 'ProductName'

    

