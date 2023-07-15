from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from library_app.author.models import Author


# class AuthorBaseForm(forms.ModelForm):
#     name = forms.CharField(
#         label='',
#         widget=forms.TextInput(attrs={'placeholder': 'Author\' full name', 'class': 'lib-form-input'})
#     )
#     bio = forms.CharField(
#         label='',
#         widget=forms.Textarea(attrs={'placeholder': 'Author\'s bio', 'class': 'lib-form-input'})
#     )
#     birth_year = forms.IntegerField(
#         label='',
#         widget=forms.NumberInput(attrs={'placeholder': 'Author\'s birth year', 'class': 'lib-form-input'})
#     )
#     death_year = forms.IntegerField(
#         label='',
#         widget=forms.NumberInput(attrs={'placeholder': 'Author\'s death year', 'class': 'lib-form-input'})
#     )
#     nationality = CountryField(blank_label='Author\'s nationality:',).formfield(
#         widget=CountrySelectWidget(attrs={"class": "lib-form-input lib-select-fix"}),
#         label='',
#     )
#     picture = forms.ImageField(
#         label='Upload author picture',
#         widget=forms.FileInput(attrs={'class': 'lib-form-input'})
#     )
#
#     class Meta:
#         model = Author
#         fields = '__all__'


class AuthorBaseForm(forms.ModelForm):
    # name = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(attrs={'placeholder': 'Author\' full name', 'class': 'lib-form-input'})
    # )
    # bio = forms.CharField(
    #     label='',
    #     widget=forms.Textarea(attrs={'placeholder': 'Author\'s bio', 'class': 'lib-form-input'})
    # )
    # birth_year = forms.IntegerField(
    #     label='',
    #     widget=forms.NumberInput(attrs={'placeholder': 'Author\'s birth year', 'class': 'lib-form-input'})
    # )
    # death_year = forms.IntegerField(
    #     label='',
    #     widget=forms.NumberInput(attrs={'placeholder': 'Author\'s death year', 'class': 'lib-form-input'})
    # )
    nationality = CountryField(blank_label='--- Nationality ---',).formfield(
        label='',
    )
    # picture = forms.ImageField(
    #     label='Upload author picture',
    #     widget=forms.FileInput(attrs={'class': 'lib-form-input'})
    # )

    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'name': '',
            'bio': '',
            'birth_year': '',
            'death_year': '',
            'nationality': '',
            'picture': 'Upload Author picture',
        }


class AuthorCreateForm(AuthorBaseForm):
    pass


class AuthorEditForm(AuthorBaseForm):
    pass


class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
