from django import forms


class SearchForm(forms.Form):
    SEARCH_CHOICES = (
        ('title', 'Search by book title'),
        ('author', 'Search by author'),
    )

    search_by = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        widget=forms.RadioSelect,
        label='',
    )

    query = forms.CharField(
        label='',
        required=False
    )
