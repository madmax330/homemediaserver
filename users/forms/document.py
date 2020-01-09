from django.forms import ModelForm

from users.models import Document


class DocumentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Document
        exclude = ('date_uploaded', 'private')


class EditDocumentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditDocumentForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Document
        exclude = ('date_uploaded', 'owner', 'private', 'document')
