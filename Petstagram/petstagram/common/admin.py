from django.contrib import admin

from petstagram.common.models import PhotoComment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'related_photo_id', 'comment_publish_date_time')


admin.site.register(PhotoComment, CommentAdmin)