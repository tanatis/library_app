from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from library_app.book.models import Book
from library_app.comments.forms import CommentForm


@login_required
def comment_add(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.to_book = book
            new_comment.user = request.user
            new_comment.save()

        return redirect(request.META['HTTP_REFERER'])
