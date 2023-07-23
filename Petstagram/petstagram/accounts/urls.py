from django.urls import path, include
from petstagram.accounts import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout', views.LogOut.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetails.as_view(), name='profile details'),
        path('edit/', views.EditProfile.as_view(), name='edit profile'),
        path('delete/', views.DeleteProfile.as_view(), name='delete profile')
    ])),
]
