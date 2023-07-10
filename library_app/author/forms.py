from django import forms

from library_app.author.models import Author


class AuthorEditForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
