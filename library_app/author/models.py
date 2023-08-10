from django.db import models
from django_countries.fields import CountryField

from library_app.core.validators import max_image_size_validator, author_birth_death_year_validator, \
    author_name_validator


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        validators=(author_name_validator,),
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    nationality = CountryField(
        null=False,
        blank=False,
    )

    birth_year = models.PositiveIntegerField(
        blank=False,
        null=False,
        validators=(author_birth_death_year_validator,),
    )

    death_year = models.IntegerField(
        blank=True,
        null=True,
        validators=(author_birth_death_year_validator,),
    )

    picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='author-images',
        validators=(max_image_size_validator,),
    )

    def __str__(self):
        return self.name
