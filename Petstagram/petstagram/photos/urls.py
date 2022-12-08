from django.urls import path, include
from petstagram.photos import views
from petstagram.common import views as commonviews
urlpatterns = [
    path('add/', views.photo_add, name='add photo'),
    path('<int:pk>/', include([
        path('', views.photo_details, name='photo details'),
        path('edit/', views.photo_edit, name='edit photo'),
        path('like/photo-<int:photo_id>/', commonviews.like_photo, name='like photo'),
        path('share/photo-<int:photo_id>/', commonviews.copy_url_to_clipboard, name='share photo'),
        path('delete/', views.photo_delete, name='delete photo')
    ])),
]

