from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def pet_add(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    tagged_photos = pet.photo_set.all()
    tagged_photos_count = tagged_photos.count()
    context = {
        'pet_name': pet.name,
        'pet_photo': pet.pet_photo,
        'pet_slug': pet_slug,
        'pet_total_photos': tagged_photos_count,
        'all_photo_objects': tagged_photos,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_delete(request, username, pet_slug):
    return render(request, template_name='pets/pet-delete-page.html')


def pet_edit(request, username, pet_slug):
    return render(request, template_name='pets/pet-edit-page.html')

