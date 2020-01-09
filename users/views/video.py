from django.shortcuts import render, Http404, redirect
from django.views.generic import View

from users.controllers.video import VideoController


def videos(request):

    if request.method == 'GET':
        controller = VideoController()
        context = {
            'videos': controller.get_videos(),
        }
        return render(request, 'users/video/index.html', context)

    raise Http404


class VideoForm(View):
    template_name = 'users/video/form.html'

    def get(self, request, key):
        controller = VideoController()
        if key > 0:
            context = {
                'video': controller.get_video(key),
                'form': controller.get_form(controller.get_video(key))
            }
        else:
            context = {
                'video': None,
                'form': controller.get_form(None)
            }

        return render(request, self.template_name, context)

    def post(self, request, key):
        controller = VideoController()
        if key > 0:
            video = controller.get_video(key)
            form = controller.edit_video(request.POST.copy(), video)
            context = {
                'video': controller.get_video(key) if form.errors else form.instance,
                'form': form,
                'message': None if form.errors else {'message': 'Video updated successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)
        else:
            info = request.POST.copy()
            info['name'] = info['name'] if info['name'] else request.FILES['video'].name
            info['owner'] = self.request.user.id
            arr = request.FILES['video'].name.split('.')
            if len(arr) > 1:
                ext = arr[len(arr) - 1]
                info['extension'] = ext
            form = controller.new_video(info, request.FILES)
            context = {
                'video': None,
                'form': form,
                'message': None if form.errors else {'message': 'Video added successfully', 'status': 'success'}
            }
            return render(request, self.template_name, context)


def delete_video(request, key):

    if request.method == 'GET':
        controller = VideoController()
        video = controller.get_video(key)
        if video is not None:
            video.delete()
            return redirect('users:videos')
        else:
            raise Http404

    raise Http404


def watch(request, key):

    if request.method == 'GET':
        controller = VideoController()
        context = {
            'video': controller.get_video(key)
        }
        return render(request, 'users/video/watch.html', context)

    raise Http404
