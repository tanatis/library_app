from django.shortcuts import render

from library_app.book.models import Book
from library_app.common.forms import SearchForm


def index(request):
    books = Book.objects.all()

    search_form = SearchForm(request.GET)
    search_pattern = None
    if search_form.is_valid():
        search_pattern = search_form.cleaned_data['book']

    if search_pattern:
        books = books.filter(title__icontains=search_pattern)
    context = {
        'books': books,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context)


def restricted(request):
    return render(request, 'common/restricted.html')
