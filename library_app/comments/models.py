from django.contrib.auth import get_user_model
from django.db import models

from library_app.book.models import Book

UserModel = get_user_model()


class Comment(models.Model):
    content = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )
    date_time_of_publication = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True,
    )
    to_book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        ordering = ['-date_time_of_publication']
