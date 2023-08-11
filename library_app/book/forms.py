from django import forms

from library_app.author.models import Author
from library_app.book.models import Book, Genre


class BookBaseForm(forms.ModelForm):
    genre = forms.TypedChoiceField(
        label='',
        choices=[('', '---   Genre:   ---')] + list(Genre.choices()),
        coerce=str,
        widget=forms.Select(attrs={'class': 'lib-form-input'})
    )

    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select(attrs={'class': 'lib-form-input'}),
        empty_label='---   Author:   ---',
        label='',
    )

    availability = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={'placeholder': 'Number of books available', 'class': 'lib-form-input'})
    )

    class Meta:
        model = Book
        fields = ('title', 'description', 'genre', 'author', 'number_of_pages', 'availability', 'cover',)
        labels = {
            'title': '',
            'description': '',
            'number_of_pages': '',
            'cover': 'Upload book cover',
        }


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass


class BookDeleteForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
