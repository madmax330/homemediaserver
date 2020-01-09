from django.forms import ModelForm

from users.models import Photo


class PhotoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Photo
        exclude = ('date_uploaded', 'private')


class EditPhotoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditPhotoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Photo
        exclude = ('date_uploaded', 'owner', 'private', 'photo')
