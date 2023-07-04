from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    consent = forms.BooleanField(
        help_text='Please read and agree'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email'})
    )

    # class Meta:
    #     model = UserModel
    #     fields = ('username', 'email')

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email')
