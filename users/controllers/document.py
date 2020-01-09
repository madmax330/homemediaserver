from django.core.exceptions import ObjectDoesNotExist

from users.models import Document

from users.forms.document import DocumentForm, EditDocumentForm

from users.display_classes import DisplayDocument


class DocumentController:

    def get_document(self, key):
        try:
            return Document.objects.get(id=key)
        except ObjectDoesNotExist:
            return None

    def get_documents(self):
        return list(map(get_display_document, Document.objects.all().order_by('name')))

    def get_form(self, doc):
        if doc is not None:
            return DocumentForm(instance=doc)
        return DocumentForm()

    def new_document(self, info, files):
        form = DocumentForm(info, files)
        if form.is_valid():
            form.save()
        return form

    def edit_document(self, info, doc):
        form = EditDocumentForm(info, instance=doc)
        if form.is_valid():
            form.save()
        return form


def get_display_document(doc):
    return DisplayDocument(doc)

