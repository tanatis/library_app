from django import forms

from library_app.borrow.models import Borrow


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ()


class SearchUserForm(forms.Form):
    user = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search user ...',
                'class': 'search-input',
            }
        )
    )
