from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.products.as_view() , name= 'products'),
    path('<slug:slug>/',views.ProductsDetail.as_view(), name='ProductsDetail'),

]