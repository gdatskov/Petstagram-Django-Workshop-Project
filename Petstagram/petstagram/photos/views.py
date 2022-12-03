from django.shortcuts import render
from django.urls import path

from petstagram.photos.models import Photo


def photo_add(request):
    return render(request, template_name='photos/photo-add-page.html')


def photo_details(request, pk):

    photo = Photo.objects.get(id=pk)

    return render(request, template_name='photos/photo-details-page.html', context={'photo': photo})


def photo_edit(request, pk):
    return render(request, template_name='photos/photo-edit-page.html')
