from django import forms

from library_app.book.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
