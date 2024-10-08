from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views.generic import CreateView
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = 'thanks/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home_index")

class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "login.html"
    def get_success_url(self):
        return redirect("home_index")

def logout(request):
    auth_logout(request)
    return redirect("home_index")
