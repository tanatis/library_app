from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from library_app.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    consent = forms.BooleanField(
        help_text='Please read and agree'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'})
    )

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')


# class ProfileCreateForm(UserCreationForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
