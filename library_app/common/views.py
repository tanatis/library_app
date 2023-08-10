from django.core.paginator import Paginator
from django.shortcuts import render
from django.core.cache import cache
from library_app.book.models import Book
from library_app.comments.models import Comment
from library_app.common.forms import SearchForm


def index(request):
    # cache only the books but not the whole view
    if not cache.get('books'):
        cache.set('books', Book.objects.all(), 60)
    books = cache.get('books')

    # Search
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        search_criteria = search_form.cleaned_data['search_by']
        query = search_form.cleaned_data['query']

        if query:
            if search_criteria == 'title':
                books = books.filter(title__icontains=query)
            elif search_criteria == 'author':
                books = books.filter(author__name__icontains=query)

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    else:
        books = books.order_by('-id')

    # Pagination
    paginator = Paginator(books, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Comments count
    book_comments_counts = {book: Comment.objects.filter(to_book=book).count() for book in books}

    context = {
        'books': books,
        'search_form': search_form,
        'page_obj': page_obj,
        'book_comments_counts': book_comments_counts,
    }
    return render(request, 'common/home-page.html', context)


def restricted(request):
    return render(request, 'common/restricted.html')


def error_page(request):
    return render(request, 'common/error.html')
