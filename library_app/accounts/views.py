from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from library_app.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from library_app.accounts.models import Profile
from library_app.borrow.models import Borrow

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('user login')
    form_class = AppUserCreationForm

    # автоматично създава празен profile вързан към новосъздадения user
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

    # prevent logged users from seeing the registration form
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class SignInView(auth_views.LoginView):
    template_name = 'accounts/user_login.html'
    form_class = AppUserLoginForm


class SignOutView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'profile/profile_details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pk'] = self.object.pk

        # TODO: without get_object_or_404
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        borrowed_books = Borrow.objects.filter(user=profile.user)
        context['borrowed_books'] = borrowed_books

        return context


    # def profile_complete(self):
    #     if self.object.first_name == '':
    #         return False
    #     return True


class ProfileEditView(UserPassesTestMixin, views.UpdateView):
    template_name = 'profile/profile_edit.html'
    model = Profile
    form_class = ProfileEditForm
    #fields = ('first_name', 'last_name', 'gender', 'profile_image',)

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})

    # Prevent accessing edit URL if not owner
    def test_func(self):
        profile = self.get_object()
        return self.request.user.is_authenticated and self.request.user == profile.user
