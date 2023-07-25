from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic as views

from library_app.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm, AppUserDeleteForm
from library_app.accounts.models import Profile
from library_app.book.models import Book
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


class AppUserChangePassword(auth_views.PasswordChangeView):
    template_name = 'accounts/change-password.html'

    def get_success_url(self):
        pk = self.request.user.pk
        return reverse_lazy('profile details', args=[pk])


class ProfileDetailsView(views.DetailView):
    template_name = 'profile/profile_details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['pk'] = self.object.pk

        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        borrowed_books = Borrow.objects.filter(user=profile.user)

        today_date = timezone.now().date()
        for book in borrowed_books:
            book.is_overdue = today_date > book.return_date

        context['borrowed_books'] = borrowed_books

        last_viewed_books_ids = self.request.session.get('last_viewed_books', [])
        context['last_viewed_books'] = Book.objects.filter(pk__in=last_viewed_books_ids)

        return context


class ProfileEditView(UserPassesTestMixin, views.UpdateView):
    template_name = 'profile/profile_edit.html'
    model = Profile
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})

    # Prevent accessing edit URL if not owner
    def test_func(self):
        profile = self.get_object()
        return self.request.user.is_authenticated and self.request.user == profile.user


@login_required
def user_delete(request, pk):
    user = UserModel.objects.filter(pk=pk).get()

    if request.user != user:
        messages.warning(request, 'You can only delete your own account!')
        return redirect('restricted')

    if request.method == 'GET':
        form = AppUserDeleteForm(instance=user)
    else:
        form = AppUserDeleteForm(request.POST, instance=user)
        if form.is_valid():
            if Borrow.objects.filter(user=user).exists():
                messages.warning(request, "You cannot delete your account until you return all borrowed books.")
                return redirect('error')
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/user_delete.html', context)
