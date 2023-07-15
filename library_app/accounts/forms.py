from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.safestring import mark_safe

from library_app.accounts.models import Profile, Gender

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    consent = forms.BooleanField(
        help_text=mark_safe('Agree with our <a href="#">terms and conditions</a>.'),
        label='',
    )
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username', 'class': 'lib-form-input'})
    # )
    # email = forms.EmailField(
    #     widget=forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email', 'class': 'lib-form-input'})
    # )
    # password1 = forms.CharField(
    #     widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'class': 'lib-form-input'})
    # )
    # password2 = forms.CharField(
    #     widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Confirm password', 'class': 'lib-form-input'})
    # )

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'consent')
        error_messages = {
            'username': {
                'unique': 'This username is already taken',
            },
            'email': {
                'unique': 'User with this email already exists'
            },
        }


class AppUserLoginForm(AuthenticationForm):
    # username = forms.CharField(
    #     widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username', 'class': 'lib-form-input'})
    # )
    # password = forms.CharField(
    #     widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Password', 'class': 'lib-form-input'})
    # )
    pass


class ProfileEditForm(forms.ModelForm):
    gender = forms.TypedChoiceField(
        label='',
        choices=[('', '---   Gender:   ---')] + list(Gender.choices()),
        coerce=str,
        # widget=forms.Select(attrs={'class': 'lib-form-input'})
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'profile_image',)
        labels ={
            'first_name': '',
            'last_name': '',
            'gender': '',
            'profile_image': 'Upload profile picture',
        }