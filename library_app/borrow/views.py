from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.utils import timezone
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from library_app.book.models import Book
from library_app.borrow.forms import BorrowBookForm
from library_app.borrow.models import Borrow
from library_app.core.functionality import get_creator_user

UserModel = get_user_model()


@login_required
@user_passes_test(get_creator_user, login_url='restricted')
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

@login_required
def borrow_book(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if book.availability > 0:
        borrow_date = timezone.now().date()
        return_date = borrow_date + timezone.timedelta(days=1)  # Assuming a 7-day borrowing period
        if request.method == 'GET':
            form = BorrowBookForm()
        else:
            form = BorrowBookForm(request.POST)

            if form.is_valid():
                user = request.user
                # Check if the user has already borrowed the same book
                if Borrow.objects.filter(user=user, book=book, return_date__gte=borrow_date).exists():
                    messages.warning(request, "You have already borrowed this book.")
                    return redirect('restricted')

                new_borrow = form.save(commit=False)
                new_borrow.borrow_date = borrow_date
                new_borrow.return_date = return_date
                new_borrow.user = user
                new_borrow.book = book
                new_borrow.save()

                book.availability -= 1
                book.borrowed_count += 1
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
        return redirect('restricted')


@login_required
@user_passes_test(get_creator_user, login_url='restricted')
def borrow_delete(request, pk):
    borrow = Borrow.objects.filter(pk=pk).get()

    book = borrow.book
    book.availability += 1
    book.borrowed_count -= 1
    book.save()
    borrow.delete()
    return redirect('borrow list')
