from django import forms


class SearchForm(forms.Form):
    # book = forms.CharField(
    #     required=False,
    #     label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder': 'Search book ...',
    #             'class': 'search-input',
    #         }
    #     )
    # )
    SEARCH_CHOICES = (
        ('title', 'Search by book title'),
        ('author', 'Search by author'),
    )

    search_by = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        widget=forms.RadioSelect,
        label='',
        #initial='title',  # Set the default search criteria to 'title'
    )

    query = forms.CharField(
        label='',
        required=False
    )
