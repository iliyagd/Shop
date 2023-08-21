from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('',views.Blog.as_view() , name= 'blog'),
    path('<slug:slug>/',views.BlogDetail.as_view(), name='BlogDetail'),
]