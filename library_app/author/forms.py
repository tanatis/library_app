from django import forms
from django_countries.fields import CountryField

from library_app.author.models import Author


class AuthorBaseForm(forms.ModelForm):
    nationality = CountryField(blank_label='--- Nationality ---',).formfield(
        label='',
    )

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
