from enum import Enum

from django.db import models

from library_app.author.models import Author
from library_app.core.validators import max_image_size_validator


class Genre(Enum):
    romance = 'Romance'
    mystery = 'Mystery'
    thriller = 'Thriller'
    science = 'Science'
    fiction = 'Fiction'
    fantasy = 'Fantasy'
    horror = 'Horror'
    historical = 'Historical'
    adventure = 'Adventure'
    children = 'Children'
    drama = 'Drama'
    comedy = 'Comedy'
    poetry = 'Poetry'
    classic = 'Classic'
    literature = 'Literature'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def length(cls):
        return max(len(name) for name, _ in cls.choices())


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    genre = models.CharField(
        blank=False,
        null=False,
        choices=Genre.choices(),
        max_length=Genre.length(),
    )

    availability = models.IntegerField(
        blank=False,
        null=False,
        default=1,
    )

    cover = models.ImageField(
        blank=False,
        null=False,
        validators=(max_image_size_validator,),
        upload_to='book-covers'
    )

    number_of_pages = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    borrowed_count = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
