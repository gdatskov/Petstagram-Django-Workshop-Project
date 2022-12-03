from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse

from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_photo_url
from petstagram.photos.models import Photo

from pyperclip import copy as pypercopy


def index(request):
    all_photo_objects = Photo.objects.all()

    context = {
        'all_photo_objects': all_photo_objects
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(related_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        # save() is used for creation/update
        # PhotoLike(related_photo=photo).save()

        # Or If it only has to be created:
        PhotoLike.objects.create(related_photo=photo)

    return redirect(get_photo_url(request, photo_id))


def copy_url_to_clipboard(request, photo_id):
    # Variant 1:
    # url = get_photo_url(request, photo_id)

    # Variant 2 (meh):
    # url = request.META['HTTP_HOST'] + reverse('photo details', kwargs={'pk': photo_id})

    # Variant 3:
    url = request.META['HTTP_HOST'] + resolve_url('photo details', photo_id)

    # NOTE: pyperclip requires additional libraries to work on Linux - e.g. it works for Windows and Mac only
    pypercopy(url)

    return redirect(get_photo_url(request, photo_id))

