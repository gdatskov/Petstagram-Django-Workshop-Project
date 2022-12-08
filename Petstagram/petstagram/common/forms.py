from django import forms

from petstagram.common.models import PhotoComment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...'
                }
            )
        }


class SearchForm(forms.Form):
    pet_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search pet by name...'
            }
        )
    )
