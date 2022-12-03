from django.contrib import admin

from petstagram.pets.models import Pet


# admin.site.register(Pet)


# Change how pets are shown in admin site:
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pet_slug')


admin.site.register(Pet, PetAdmin)

