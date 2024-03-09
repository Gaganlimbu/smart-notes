from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    http_method_names = ['get', 'post']
    extra_context = {'today': datetime.today()}

    def get_success_url(self):
        return reverse_lazy('home')


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'
