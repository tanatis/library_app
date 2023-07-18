from django.shortcuts import render
from django.core.cache import cache
from library_app.book.models import Book
from library_app.common.forms import SearchForm


def index(request):
    #books = Book.objects.all()
    # кешираме само книгите, а не цялото вю
    if not cache.get('books'):
        cache.set('books', Book.objects.all(), 60)
    books = cache.get('books')

    # search_form = SearchForm(request.GET)
    # search_pattern = None
    # if search_form.is_valid():
    #     search_pattern = search_form.cleaned_data['book']
    #
    # if search_pattern:
    #     books = books.filter(title__icontains=search_pattern)

    search_form = SearchForm(request.GET)
    #search_criteria = 'title'  # Default search criteria

    if search_form.is_valid():
        search_criteria = search_form.cleaned_data['search_by']
        query = search_form.cleaned_data['query']

        if query:
            if search_criteria == 'title':
                books = books.filter(title__icontains=query)
            elif search_criteria == 'author':
                books = books.filter(author__name__icontains=query)

    sort_by = request.GET.get('sort_by')
    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    # Add more sorting options here if needed
    else:
        # By default, sort by ID if no sorting option is selected
        books = books.order_by('-id')

    context = {
        'books': books,
        'search_form': search_form,
    }
    return render(request, 'common/home-page.html', context)


def restricted(request):
    return render(request, 'common/restricted.html')
