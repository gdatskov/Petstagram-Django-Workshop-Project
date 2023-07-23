from django import forms

from petstagram.photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['photo_publish_date', 'photo_user']
        # fields = ['photo', 'photo_description', 'photo_location', 'photo_tagged_pets']
        labels = {
            'photo': 'Photo file',
            'photo_description': 'Description',
            'photo_location': 'Location',
            'photo_tagged_pets': 'Tag Pets',
        }
        # No Effect...
        # widgets = {
        #     'photo_tagged_pets': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 4}),
        # }


class AddPhotoForm(PhotoForm):
    pass


class EditPhotoForm(PhotoForm):
    pass


class DeletePhotoForm(PhotoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

