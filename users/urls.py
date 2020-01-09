from django.urls import path

from users.views import index
from users.views import video
from users.views import document
from users.views import photo

app_name = 'users'
urlpatterns = [
    path('videos/', video.videos, name='videos'),
    path('photos/', photo.photos, name='photos'),
    path('documents/', document.documents, name='documents'),

    path('video/form/<int:key>/', video.VideoForm.as_view(), name='video_form'),
    path('photo/form/<int:key>/', photo.PhotoForm.as_view(), name='photo_form'),
    path('document/form/<int:key>/', document.DocumentForm.as_view(), name='document_form'),

    path('video/<int:key>/', video.watch, name='watch'),
    # path('document/<int:key>/', document.show_document, name='show_document'),

    path('video/delete/<int:key>/', video.delete_video, name='delete_video'),
    path('photo/delete/<int:key>/', photo.delete_photo, name='delete_photo'),
    path('document/delete/<int:key>/', document.delete_document, name='delete_document'),

    path('', index.index, name='index'),
]

