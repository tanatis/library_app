from django import forms

from library_app.book.models import Book


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass
