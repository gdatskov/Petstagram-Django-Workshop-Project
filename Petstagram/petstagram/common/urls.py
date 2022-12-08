from django.urls import path, include
from petstagram.common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('like/photo-<int:photo_id>/', views.like_photo, name='like photo'),
    path('share/photo-<int:photo_id>/', views.copy_url_to_clipboard, name='share photo'),
    path('comment/photo-<int:photo_id>', views.add_comment, name='add comment')

]
