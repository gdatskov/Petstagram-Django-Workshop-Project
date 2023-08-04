from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from petstagram.common.forms import AddCommentForm
from petstagram.pets.forms import AddPetForm, EditPetForm, DeletePetForm
from petstagram.pets.models import Pet
from petstagram.pets.utils import get_pet_by_slug_and_username, is_owner
from petstagram.photos.models import Photo


@login_required
def pet_add(request):
    if request.method == 'GET':
        form = AddPetForm()
    else:
        form = AddPetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.pet_user = request.user
            pet.save()
            # return redirect('profile details', pk=pet.pet_user.pk)
            return redirect('pet details', username=pet.pet_user.username, pet_slug=pet.pet_slug)

    context = {'add_pet_form': form}

    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    tagged_pet_photo_objects = Photo.objects.filter(photo_tagged_pets__pet_slug=pet_slug).all()
    pet = get_pet_by_slug_and_username(pet_slug, username)
    tagged_photos = pet.photo_set.all()
    tagged_photos_count = tagged_photos.count()
    context = {
        'pet_name': pet.name,
        'pet_photo': pet.pet_photo,
        'pet_slug': pet_slug,
        'pet_total_photos': tagged_photos_count,
        'tagged_photos': tagged_photos,
        'photo_comment_form': AddCommentForm(),
        'is_owner': pet.pet_user == request.user,
        'all_photo_objects': tagged_pet_photo_objects,
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = get_pet_by_slug_and_username(pet_slug, username)

    if request.method == 'GET':
        form = DeletePetForm(instance=pet)
    else:
        pet.delete()
        return redirect('profile details', pk=1)

    context = {'delete_pet_form': form}
    return render(request, template_name='pets/pet-delete-page.html', context=context)


def pet_edit(request, username, pet_slug):
    print(username)
    pet = get_pet_by_slug_and_username(pet_slug, username)

    # url tampering defence
    if not is_owner(request, pet.pet_user):
        return redirect('pet details', username=username, pet_slug=pet_slug)  # or redirect anywhere else

    if request.method == 'GET':
        form = EditPetForm(instance=pet)
    else:
        form = EditPetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)

    context = {'edit_pet_form': form}
    return render(request, template_name='pets/pet-edit-page.html', context=context)

