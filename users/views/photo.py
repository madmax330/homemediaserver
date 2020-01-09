from django.shortcuts import render, Http404, redirect
from django.views.generic import View

from users.controllers.photo import PhotoController


def photos(request):

    if request.method == 'GET':
        controller = PhotoController()
        context = {
            'photos': controller.get_photos(),
        }
        return render(request, 'users/photos/index.html', context)

    raise Http404


class PhotoForm(View):
    template_name = 'users/photos/form.html'

    def get(self, request, key):
        controller = PhotoController()
        if key > 0:
            context = {
                'photo': controller.get_photo(key),
                'form': controller.get_form(controller.get_photo(key))
            }
        else:
            context = {
                'photo': None,
                'form': controller.get_form(None)
            }

        return render(request, self.template_name, context)

    def post(self, request, key):
        controller = PhotoController()
        if key > 0:
            photo = controller.get_photo(key)
            form = controller.edit_photo(request.POST.copy(), photo)
            context = {
                'photo': controller.get_photo(key) if form.errors else form.instance,
                'form': form,
                'message': None if form.errors else {'message': 'Photo updated successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)
        else:
            info = request.POST.copy()
            info['name'] = info['name'] if info['name'] else request.FILES['photo'].name
            info['owner'] = self.request.user.id
            form = controller.new_photo(info, request.FILES)
            context = {
                'photo': None,
                'form': form,
                'message': None if form.errors else {'message': 'Photo added successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)


def delete_photo(request, key):

    if request.method == 'GET':
        controller = PhotoController()
        photo = controller.get_photo(key)
        if photo is not None:
            photo.delete()
            return redirect('users:photos')
        else:
            raise Http404

    raise Http404
