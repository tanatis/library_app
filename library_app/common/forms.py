from django import forms


class SearchForm(forms.Form):
    book = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search book ...',
                'class': 'search-input',
            }
        )
    )
