
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from .forms import SearchForm
from django.db.models import Q

from .models import product
from .models import Category, ArticleSerachLog

class products(ListView):
    model = product
    template_name = 'product.html'
    context_object_name = 'products'
    def get_queryset(self) -> QuerySet[Any]:
        queryset = self.model.objects.all()
        search_filter = self.request.GET.get('search',None)
        if search_filter:
            ArticleSerachLog.objects.create(body=search_filter)
            queryset = queryset.filter(Q(ProductName_icontains=search_filter))
        return queryset.distinct()
class Category(ListView):
    template_name = 'Category.html'
    model = Category
    context_object_name = 'Categorys'
    
    
class ProductsDetail(DetailView):
    template_name = 'productView.html'
    model = product
    context_object_name = 'products'
    slug_field = 'ProductName'



    




