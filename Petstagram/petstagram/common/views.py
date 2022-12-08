from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from petstagram.common.forms import AddCommentForm, SearchForm
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_photo_url
from petstagram.photos.models import Photo

from pyperclip import copy as pypercopy


def index(request):
    all_photo_objects = Photo.objects.all()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_pattern = search_form.cleaned_data['pet_name']
            all_photo_objects = all_photo_objects.filter(photo_tagged_pets__name__icontains=search_pattern)

    context = {
        'all_photo_objects': all_photo_objects,
        'photo_comment_form': AddCommentForm(),
        'search_form': search_form,
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


def add_comment(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    # No need... Only POST method
    # if request.method == 'GET':
    #     form = AddCommentForm(instance=photo)
    # else:
    form = AddCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.related_photo_id = photo.id
        comment.save()

    # context = {'add_comment_form': form}
    # return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')
    return redirect(get_photo_url(request, photo_id))
