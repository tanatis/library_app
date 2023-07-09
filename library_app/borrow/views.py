from django.utils import timezone

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from library_app.book.models import Book
from library_app.borrow.forms import BorrowBookForm
from library_app.borrow.models import Borrow

UserModel = get_user_model()


def borrow_list(request):
    borrows = Borrow.objects.all()
    return render(request, 'common/borrow_list.html', {'borrows': borrows})


# def borrow_book(request, book_pk):
#     book = Book.objects.filter(pk=book_pk).get()
#
#     if book.availability > 0:
#         borrow_date = timezone.now().date()
#         return_date = borrow_date + timezone.timedelta(days=7)  # Assuming a 7-day borrowing period
#
#         # Create a new Borrow instance
#         new_borrow = Borrow.objects.create(
#             borrow_date=borrow_date,
#             return_date=return_date,
#             user=request.user,
#             book=book
#         )
#         book.availability -= 1
#         book.save()
#
#         context = {
#             'book': book,
#             'return_date': return_date,
#             'author': book.author,
#             'new_borrow': new_borrow,
#         }
#         return render(request, 'common/borrow.html', context)
#
#     else:
#         return redirect('index')

def borrow_book(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if book.availability > 0:
        borrow_date = timezone.now().date()
        return_date = borrow_date + timezone.timedelta(days=7)  # Assuming a 7-day borrowing period
        if request.method == 'GET':
            form = BorrowBookForm()
        else:
            form = BorrowBookForm(request.POST)

            if form.is_valid():
                new_borrow = form.save(commit=False)
                new_borrow.borrow_date = borrow_date
                new_borrow.return_date = return_date
                new_borrow.user = request.user
                new_borrow.book = book
                new_borrow.save()

                book.availability -= 1
                book.save()

                return redirect('index')
        context = {
            'form': form,
            'book': book,
            'author': book.author,
            'return_date': return_date,
        }
        return render(request, 'common/borrow.html', context)
    else:
        return redirect('index')

def borrow_delete(request, pk):
    borrow = Borrow.objects.filter(pk=pk).get()

    book = borrow.book
    book.availability += 1
    book.save()
    borrow.delete()
    return redirect('borrow list')
