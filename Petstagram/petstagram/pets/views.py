from django.shortcuts import render, redirect

from petstagram.common.forms import AddCommentForm
from petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def pet_add(request):
    if request.method == 'GET':
        form = AddPetForm()
    else:
        form = AddPetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=1)

    context = {'add_pet_form': form}

    return render(request, template_name='pets/pet-add-page.html', context=context)


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
        'photo_comment_form': AddCommentForm()
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    if request.method == 'GET':
        form = DeletePetForm(instance=pet)
    else:
        pet.delete()
        return redirect('profile details', pk=1)

    context = {'delete_pet_form': form}
    return render(request, template_name='pets/pet-delete-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    if request.method == 'GET':
        form = EditPetForm(instance=pet)
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)

    context = {'edit_pet_form': form}
    return render(request, template_name='pets/pet-edit-page.html', context=context)

