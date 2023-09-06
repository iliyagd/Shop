from django.shortcuts import render
from django.views import View
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy




class UserLogin(auth_views.LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home:home')

class UserLogout(auth_views.LogoutView):
    next_page = reverse_lazy('home:home')    