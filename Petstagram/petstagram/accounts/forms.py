from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, UserChangeForm

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
        field_classes = {"username": UsernameField}


class EditForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'gender')
        exclude = ('password',)
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'E-mail:',
            'profile_picture': 'Image:',
            'gender': 'Gender:',
        }

