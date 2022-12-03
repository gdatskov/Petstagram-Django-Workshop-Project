# Generated by Django 4.1.3 on 2022-12-01 00:45

import django.core.validators
from django.db import migrations, models
import petstagram.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "photo_publish_date",
                    models.DateField(auto_created=True, auto_now=True),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="mediafiles/pet_photos",
                        validators=[petstagram.validators.MaxSizeValidator(5)],
                    ),
                ),
                (
                    "photo_description",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("photo_location", models.CharField(max_length=30)),
                (
                    "photo_tagged_pets",
                    models.ManyToManyField(blank=True, to="pets.pet"),
                ),
            ],
        ),
    ]
