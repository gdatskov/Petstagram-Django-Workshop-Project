from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'pet_birth_date', 'pet_photo')
        labels = {
            'name': 'Pet name',
            'pet_birth_date': 'Date of birth',
            'pet_photo': 'Link to image'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet Name'
                }
            ),
            'pet_birth_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'dd/mm/yyyy'
                },
            ),
            'pet_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image'
                },
            ),
        }


class AddPetForm(PetForm):
    pass


class EditPetForm(PetForm):
    pass


class DeletePetForm(PetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
