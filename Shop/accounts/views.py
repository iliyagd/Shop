from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login 
from django.views.generic import FormView
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home:home') 
       