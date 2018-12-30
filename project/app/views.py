from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from .forms import EmailAuthenticationForm
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Top(View):
    """Base View"""

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'top.html')

    @method_decorator(login_required)
    def post(self, request):
        return render(request, 'top.html')


class Login(LoginView):
    """Login View"""
    form_class = EmailAuthenticationForm
    template_name = 'registration/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """LoginRequiredMixinでログイン確認"""
    template_name = 'top.html'
    login_url = '/email_login/login/'