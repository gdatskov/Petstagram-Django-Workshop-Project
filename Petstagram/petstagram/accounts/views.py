from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views# LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as generic_views # CreateView, DetailView, UpdateView

from petstagram.accounts.forms import RegisterForm, EditForm
from petstagram.accounts.models import Gender

# Always get UserModel with get_user_model():
UserModel = get_user_model()


class Login(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    fields = ('username', 'password')
    next_page = reverse_lazy('index')


class Register(generic_views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')


class LogOut(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileDetails(generic_views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check if user has access
        context['is_owner'] = self.request.user.pk == self.object.pk

        # Count stuff - filter by profile user id
        context['user_total_pets_count'] = self.object.pet_set.filter(pet_user_id=self.object.id).count()
        context['user_total_likes_count'] = self.object.photolike_set.filter(like_user_id=self.object.id).count()
        context['user_total_photos_count'] = self.object.photo_set.filter(photo_user_id=self.object.id).count()


        return context


class EditProfile(generic_views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile-edit-page.html'
    # fields = '__all__'
    form_class = EditForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.object.pk
        })
        # return reverse_lazy('index')


class DeleteProfile(generic_views.DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'

    def get_success_url(self):
        return reverse_lazy('index')


#
# def profile_delete(request, pk):
#     return render(request, template_name='accounts/profile-delete-page.html')


# def profile_details(request, pk):
#     return render(request, template_name='accounts/profile-details-page.html')
#
#
# def profile_edit(request, pk):
#     return render(request, template_name='accounts/profile-edit-page.html')

# def login(request):
#     return render(request, template_name='accounts/login-page.html')

# def register(request):
#     return render(request, template_name='accounts/register-page.html')
