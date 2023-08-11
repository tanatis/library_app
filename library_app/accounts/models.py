from enum import Enum

from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django.utils import timezone

from library_app.core.validators import username_validator, only_letters_validator, max_image_size_validator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'username'

    objects = UserManager()

    username = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        validators=(MinLengthValidator(3), username_validator),
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True
    )

    date_joined = models.DateTimeField(
        default=timezone.now
    )


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    hidden = 'Hidden'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def length(cls):
        return max(len(name) for name, _ in cls.choices())


class Profile(models.Model):
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=(MinLengthValidator(2), only_letters_validator)
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        validators=(MinLengthValidator(2), only_letters_validator)
    )

    gender = models.CharField(
        blank=True,
        null=True,
        choices=Gender.choices(),
        max_length=Gender.length(),
    )

    profile_image = models.ImageField(
        blank=True,
        null=True,
        upload_to='profile-images/',
        validators=(max_image_size_validator,),
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,  # pk на UserModel става pk на Profile (т.е. Profile вече няма pk в базата)
    )
