from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    COMMENT_TEXT_MAX_LEN = 300


    comment_text = models.CharField(
        max_length=COMMENT_TEXT_MAX_LEN,
        null=False,
        blank=False,
    )

    comment_publish_date_time = models.DateTimeField(
        auto_now_add=True,
        auto_created=True,
        editable=False,
    )

    related_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-comment_publish_date_time']

class PhotoLike(models.Model):
    related_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE
    )