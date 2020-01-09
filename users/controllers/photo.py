from django.core.exceptions import ObjectDoesNotExist

from users.models import Photo

from users.forms.photo import PhotoForm, EditPhotoForm


class PhotoController:

    def get_photo(self, key):
        try:
            return Photo.objects.get(id=key)
        except ObjectDoesNotExist:
            return None

    def get_photos(self):
        return Photo.objects.all()

    def get_form(self, photo):
        if photo is not None:
            return PhotoForm(instance=photo)
        return PhotoForm()

    def new_photo(self, info, files):
        form = PhotoForm(info, files)
        if form.is_valid():
            form.save()
        return form

    def edit_photo(self, info, photo):
        form = EditPhotoForm(info, instance=photo)
        if form.is_valid():
            form.save()
        return form


