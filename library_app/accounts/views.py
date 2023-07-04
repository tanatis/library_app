from django.contrib.auth import get_user_model
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from library_app.accounts.forms import AppUserCreationForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('user login')
    form_class = AppUserCreationForm

    # prevent logged users from seeing the registration form
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(SignUpView, self).get(request, *args, **kwargs)


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user_login.html'


class SignOutView(auth_views.LogoutView):
    pass
