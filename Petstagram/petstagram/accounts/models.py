from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.core import validators as builtin_validators
import petstagram.validators as custom_validators
from django.db import models


class EnumChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(parameter_name) for parameter_name, value in cls.choices())


# Another way to generate stuff
class Gender(EnumChoicesMixin):
    # DB name = Shown name
    male = 'Male'
    female = 'Female'
    do_not_show = 'Do Not Show'


# USERS MODEL MUST BE CREATED FIRST IN ANY PROJECT
# Otherwise, delete (drop the DB) and create it anew
class AppUser(AbstractUser):    # Why not use User class as parent?
    """
     The first and last names of each user should have a
        minimum length of 2,
        maximum length of 30.
        only alphabetical letters

    Each registered email in the app must be unique.

    The gender is a choice field where the user can choose between "Male", "Female" and "Do not show" options
    """

    NAME_MIN_LEN = 2
    NAME_MAX_LEN = 30

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            builtin_validators.MinLengthValidator(NAME_MIN_LEN),
            custom_validators.string_is_alpha,
        ],
        blank=False,
        null=False
    )

    last_name = models.CharField(
        "last name",
        max_length=NAME_MAX_LEN,
        validators=[
            builtin_validators.MinLengthValidator(NAME_MIN_LEN),
            custom_validators.string_is_alpha,
        ],
        blank=False,
        null=False
    )

    email = models.EmailField(unique=True)

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len()
    )
