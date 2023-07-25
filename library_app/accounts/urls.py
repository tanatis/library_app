from django.urls import path

from library_app.accounts.views import SignUpView, SignOutView, SignInView, ProfileDetailsView, ProfileEditView, \
    AppUserChangePassword, user_delete

urlpatterns = [
    path('register/', SignUpView.as_view(), name='user register'),
    path('logout/', SignOutView.as_view(), name='user logout'),
    path('login/', SignInView.as_view(redirect_authenticated_user=True), name='user login'),
    path('change-password/', AppUserChangePassword.as_view(), name='change password'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/<int:pk>/edit/', ProfileEditView.as_view(), name='profile edit'),
    path('profile/<int:pk>/delete/', user_delete, name='delete account'),
]
