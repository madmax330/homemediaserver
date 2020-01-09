from django.shortcuts import render, Http404, redirect
from django.views.generic import View

from users.controllers.document import DocumentController


def documents(request):

    if request.method == 'GET':
        controller = DocumentController()
        context = {
            'documents': controller.get_documents(),
        }
        return render(request, 'users/document/index.html', context)

    raise Http404


class DocumentForm(View):
    template_name = 'users/document/form.html'

    def get(self, request, key):
        controller = DocumentController()
        if key > 0:
            context = {
                'document': controller.get_document(key),
                'form': controller.get_form(controller.get_document(key))
            }
        else:
            context = {
                'document': None,
                'form': controller.get_form(None)
            }

        return render(request, self.template_name, context)

    def post(self, request, key):
        controller = DocumentController()
        if key > 0:
            document = controller.get_document(key)
            form = controller.edit_document(request.POST.copy(), document)
            context = {
                'document': controller.get_document(key) if form.errors else form.instance,
                'form': form,
                'message': None if form.errors else {'message': 'Document updated successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)
        else:
            info = request.POST.copy()
            info['name'] = info['name'] if info['name'] else request.FILES['document'].name
            info['owner'] = self.request.user.id
            form = controller.new_document(info, request.FILES)
            context = {
                'document': None,
                'form': form,
                'message': None if form.errors else {'message': 'Document added successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)


def delete_document(request, key):

    if request.method == 'GET':
        controller = DocumentController()
        document = controller.get_document(key)
        if document is not None:
            document.delete()
            return redirect('users:documents')
        else:
            raise Http404

    raise Http404

