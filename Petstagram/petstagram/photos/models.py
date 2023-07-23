from django.contrib.auth import get_user_model
from django.db import models

from petstagram.pets.models import Pet

from django.core import validators as builtin_validators
from petstagram import validators as custom_validators

UserModel = get_user_model()


class Photo(models.Model):
    PHOTO_DESC_MIN_LEN = 10
    PHOTO_DESC_MAX_LEN = 300
    PHOTO_LOCATION_MAX_LEN = 30
    PHOTO_MAX_SIZE_MB = 5

    photo = models.ImageField(
        null=False,
        blank=False,
        validators=([custom_validators.MaxSizeValidator(PHOTO_MAX_SIZE_MB)]),
        upload_to='pet_photos/'
    )

    photo_description = models.CharField(
        max_length=PHOTO_DESC_MAX_LEN,
        validators=([builtin_validators.MinLengthValidator(PHOTO_DESC_MIN_LEN)]),
        null=True,
        blank=True,
    )

    photo_location = models.CharField(
        max_length=PHOTO_LOCATION_MAX_LEN,
        null=False,
        blank=False,
    )

    photo_tagged_pets = models.ManyToManyField(Pet, blank=True)

    photo_publish_date = models.DateField(
        auto_now=True,
        auto_created=True,
        editable=False,
    )

    photo_user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return self.photo_description

