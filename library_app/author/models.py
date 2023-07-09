from django.db import models
from django_countries.fields import CountryField

from library_app.core.validators import max_image_size_validator


class Author(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        # TODO: validate name
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    nationality = CountryField(
        null=False,
        blank=False,
    )

    # TODO: Years only
    # birth_date = models.DateField(
    #     blank=False,
    #     null=False,
    # )
    #
    # death_date = models.DateField(
    #     blank=True,
    #     null=True,
    # )

    # picture = models.ImageField(
    #     blank=True,
    #     null=True,
    #     upload_to='author-images',
    #     validators=(max_image_size_validator,),
    # )

    def __str__(self):
        return self.name
