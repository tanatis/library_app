from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from library_app.book.models import Book
from library_app.borrow.forms import BorrowBookForm, SearchUserForm
from library_app.borrow.models import Borrow
from library_app.core.functionality import get_creator_user

UserModel = get_user_model()


@login_required
#@user_passes_test(get_creator_user, login_url='restricted')
def borrow_list(request):
    if not get_creator_user(request.user):
        messages.error(request, "You don't have permissions to access this page")
        return redirect('restricted')

    borrows = Borrow.objects.all()

    search_user_form = SearchUserForm(request.GET)
    search_pattern = None
    if search_user_form.is_valid():
        search_pattern = search_user_form.cleaned_data['user']

    if search_pattern:
        borrows = borrows.filter(user__username__icontains=search_pattern)

    ###############################################

    today_date = timezone.now().date()
    for borrow in borrows:
        borrow.is_overdue = today_date > borrow.return_date

    context = {
        'borrows': borrows,
        'form': search_user_form,
    }
    return render(request, 'common/borrow_list.html', context)


@login_required
def borrow_book(request, book_pk):
    book = Book.objects.filter(pk=book_pk).get()

    if book.availability > 0:
        days_to_return = 1
        borrow_date = timezone.now().date()
        return_date = borrow_date + timezone.timedelta(days=days_to_return)
        if request.method == 'GET':
            form = BorrowBookForm()
        else:
            form = BorrowBookForm(request.POST)

            if form.is_valid():
                user = request.user
                # Check if the user has already borrowed the same book
                if Borrow.objects.filter(user=user, book=book, return_date__gte=borrow_date).exists():
                    messages.warning(request, "You have already borrowed this book.")
                    return redirect('error')

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
def borrow_delete(request, pk):
    if not get_creator_user(request.user):
        messages.error(request, "You don't have permissions to access this page")
        return redirect('restricted')

    borrow = Borrow.objects.filter(pk=pk).get()

    book = borrow.book
    book.availability += 1
    book.borrowed_count -= 1
    book.save()
    borrow.delete()
    return redirect('borrow list')


@login_required
def send_email_reminder(request, pk):
    if not get_creator_user(request.user):
        messages.error(request, "You don't have permissions to access this page")
        return redirect('restricted')

    borrow = Borrow.objects.filter(pk=pk).get()
    email = borrow.user.email
    book = borrow.book.title
    date = borrow.return_date
    send_mail(
        subject='reminder',
        message=f'Kindly reminding you that the last day to return the book "{book}" was {date}.\n Please make sure you return it ASAP.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(email,)
    )
    return redirect('borrow list')
