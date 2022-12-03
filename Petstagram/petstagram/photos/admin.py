from django.contrib import admin

from petstagram.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_description', 'id', 'photo_publish_date', 'tagged_pets_in_photo')

    @staticmethod
    def tagged_pets_in_photo(obj):
        return ', '.join([pet.name for pet in obj.photo_tagged_pets.all()])


admin.site.register(Photo, PhotoAdmin)


