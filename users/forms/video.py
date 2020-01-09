from django.forms import ModelForm

from users.models import Video


class VideoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Video
        exclude = ('date_uploaded', 'private')


class EditVideoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditVideoForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Video
        exclude = ('date_uploaded', 'owner', 'private', 'video', 'extension')
