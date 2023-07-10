from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from library_app.book.forms import BookCreateForm, BookEditForm
from library_app.book.models import Book
from library_app.core.functionality import get_creator_user


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
@user_passes_test(get_creator_user, login_url='restricted')
def book_add(request):
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'books/book_add.html', context)


@login_required
@user_passes_test(get_creator_user, login_url='restricted')
def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('all books')
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/book_edit.html', context)
