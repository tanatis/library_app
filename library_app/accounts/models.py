from django.contrib.auth.models import UserManager
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from django.utils import timezone

from library_app.core.validators import username_validator, only_letters_validator, max_image_size_validator


#UserModel = get_user_model()

# class AppUserManager(auth_models.BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, username, email, password, **extra_fields):
#         if not username:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)
#
#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#
#         return self._create_user(username, email, password, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'username'

    objects = UserManager()

    username = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        validators=(MinLengthValidator(3), username_validator)
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

    # profile -> video 3:02:30


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
        max_length=6,
        choices=(
            ('male', 'Male'),
            ('female', 'Female'),
            ('hidden', 'Hidden'),
        )
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
