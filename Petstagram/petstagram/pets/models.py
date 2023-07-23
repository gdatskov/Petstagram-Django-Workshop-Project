from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

UserModel = get_user_model()


class Pet(models.Model):
    MAX_NAME_LEN = 30
    name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=False,
        blank=False,
    )
    pet_photo = models.URLField(
        null=False,
        blank=False,
    )
    pet_birth_date = models.DateField(
        blank=True,
        null=True,
    )
    pet_slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )
    pet_user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT
    )

    # modify built-in save() in django ORM
    def save(self, *args, **kwargs):
        # Create or update (get id)
        super().save(*args, **kwargs)

        # Always check if exists to keep url consistency in case of update
        if not self.pet_slug:
            self.pet_slug = slugify(f'{self.name}-{self.id}')
            # Update again (in case of change)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
