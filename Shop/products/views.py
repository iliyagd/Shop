
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from .forms import SearchForm
from django.db.models import Q
from django.shortcuts import render, redirect

from .models import product
from .models import Category, ArticleSerachLog, CartItem

class products(ListView):
    model = product
    template_name = 'product.html'
    context_object_name = 'products'
    def get_queryset(self) -> QuerySet[Any]:
        queryset = self.model.objects.all()
        search_filter = self.request.GET.get('search',None)
        if search_filter:
            ArticleSerachLog.objects.create(body=search_filter)
            queryset = queryset.filter(Q(ProductName__icontains=search_filter))
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

class ShoppingCartView(View):
    def get(self, request):
        cart_items = request.session.get('cart_items', [])
        return render(request, 'shopping_cart.html', {'cart_items': cart_items})

    def post(self, request):
        item = request.POST.get('item')
        cart_items = request.session.get('cart_items', [])
        cart_items.append(item)
        request.session['cart_items'] = cart_items
        return redirect('products:cart')
    


from django.views.generic.edit import FormView
from . forms import Image
class UploadImageView(FormView):
    template_name = 'upload_image.html'    
    form_class = Image
    success_url = '/success/'
    def form_valid(self, form):
        return super().form_valid(form)


    




