from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from library_app.book.forms import BookCreateForm
from library_app.book.models import Book


def list_books(request):
    return render(request, 'books/book_list.html')


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    context = {
        'book': book,
        'book_pk': book.pk,
    }

    return render(request, 'books/book_details.html', context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Creator').exists(), login_url='restricted')
def book_add(request):
    form = BookCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'books/book_add.html', context)


@login_required
@user_passes_test(lambda user: user.groups.filter(name='Creator').exists(), login_url='restricted')
def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()
    form = BookCreateForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('all books')
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/book_edit.html', context)
