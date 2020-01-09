from django.contrib.auth.models import User
from django.db import models


PHOTO_EXTENSIONS = [
    'jpeg', 'jpg', 'gif', 'png', 'svg'
]

VIDEO_EXTENSIONS = [
    'avi', 'mp4', 'mov', 'm4v', 'mkv', 'flv', 'wmv', 'mpg', 'mpeg'
]


def get_file_path(instance, filename):
    return 'user_{0}/{1}/{2}'.format(instance.owner.id, get_file_type(filename), filename)


def get_file_type(name):
    arr = name.split('.')
    ext = arr[len(arr)-1].lower()
    if ext in PHOTO_EXTENSIONS:
        return 'images'
    elif ext in VIDEO_EXTENSIONS:
        return 'videos'
    else:
        return 'documents'


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to=get_file_path)
    occasion = models.CharField(max_length=100)
    private = models.BooleanField(default=False)


class Video(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to=get_file_path)
    type = models.CharField(max_length=20)
    extension = models.CharField(max_length=10)
    private = models.BooleanField(default=False)


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to=get_file_path)
    group = models.CharField(max_length=100)
    private = models.BooleanField(default=False)


class FileShare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=100)
    file_type = models.CharField(max_length=15)










