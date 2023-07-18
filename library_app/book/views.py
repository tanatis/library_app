from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from library_app.book.forms import BookCreateForm, BookEditForm, BookDeleteForm
from library_app.book.models import Book
from library_app.comments.forms import CommentForm
from library_app.core.functionality import get_creator_user


def list_books(request):
    return render(request, 'books/book_list.html')


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    comment_form = CommentForm()

    last_viewed_books = request.session.get('last_viewed_books', [])
    if book.id not in last_viewed_books:
        last_viewed_books.append(book.pk)
    #start_index = max(0, len(last_viewed_books) - 3)
    #request.session['last_viewed_books'] = last_viewed_books[start_index:]
    request.session['last_viewed_books'] = last_viewed_books[:-4:-1]

    context = {
        'book': book,
        'book_pk': book.pk,
        "comments": book.comment_set.all(),
        "comment_form": comment_form,
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


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if book.borrowed_count == 0:
        if request.method == 'GET':
            form = BookDeleteForm(instance=book)
        else:
            form = BookDeleteForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('index')
    else:
        messages.warning(request, "Book cannot be delete before it is returned")
        return redirect('restricted')
        #return redirect('restricted')  # TODO: change redirect url
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'books/book_delete.html', context)
