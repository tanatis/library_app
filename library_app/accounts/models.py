from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone


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
