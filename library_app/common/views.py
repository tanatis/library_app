from django.shortcuts import render

from library_app.book.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'common/home-page.html', context)


def restricted(request):
    return render(request, 'common/restricted.html')
