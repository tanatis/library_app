from django.urls import path

from library_app.accounts.views import SignUpView, SignOutView, SignInView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='user register'),
    path('logout/', SignOutView.as_view(), name='user logout'),
    path('login/', SignInView.as_view(redirect_authenticated_user=True), name='user login'),
]
