from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('',views.products.as_view() , name= 'products'),
    path('<slug:slug>/',views.ProductsDetail.as_view(), name='ProductsDetail'),
    path('products/cart/', views.ShoppingCartView.as_view(), name='cart'),
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),

]