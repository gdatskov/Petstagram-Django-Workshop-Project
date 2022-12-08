from django.shortcuts import render, redirect
from django.urls import path

from petstagram.common.forms import AddCommentForm
from petstagram.photos.forms import AddPhotoForm, EditPhotoForm
from petstagram.photos.models import Photo


def photo_add(request):
    if request.method == 'GET':
        form = AddPhotoForm()
    else:
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Get id for redirect: Var 1
            # last_photo_pk = Photo.objects.last().id

            # Get id for redirect directly from .save() (it returns the object anyway)
            last_photo_pk = form.save()

            return redirect('photo details', pk=last_photo_pk.id)

    context = {'add_photo_form': form}
    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = Photo.objects.get(id=pk)

    context = {
        'photo': photo,
        'photo_comment_form': AddCommentForm()
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.get(id=pk)

    if request.method == 'GET':
        form = EditPhotoForm(instance=photo)
    else:
        form = EditPhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=photo.id)

    context = {'edit_photo_form': form}

    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('index')
