from django import forms

from library_app.author.models import Author


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
