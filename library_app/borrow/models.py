from django.contrib.auth import get_user_model
from django.db import models

from library_app.book.models import Book

UserModel = get_user_model()


class Borrow(models.Model):
    borrow_date = models.DateField()

    return_date = models.DateField()

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
