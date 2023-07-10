import re

from django.core.exceptions import ValidationError


def username_validator(value):
    if not re.match("^[A-Za-z0-9_-]*$", value):
        raise ValidationError('Username can only contains letters, numbers, underscores and dashes')


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Name can only contains letters!')


def max_image_size_validator(value):
    if value.size > 1000000:
        raise ValidationError('Max file size is 1MB')


def author_name_validator(value):
    if not re.match("^[A-Za-z. ]*$", value):
        raise ValidationError('Name can only contains letters and dots!')


def author_birth_death_year_validator(value):
    if value < 1800 or value > 2020:
        raise ValidationError('Year must be between 1800 and 2020')
