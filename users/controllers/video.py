from django.core.exceptions import ObjectDoesNotExist

from users.models import Video

from users.forms.video import VideoForm, EditVideoForm

from users.display_classes import DisplayVideo


class VideoController:

    def get_video(self, key):
        try:
            return Video.objects.get(id=key)
        except ObjectDoesNotExist:
            return None

    def get_videos(self):
        return list(map(get_display_video, Video.objects.all().order_by('name')))

    def get_form(self, video):
        if video is not None:
            return VideoForm(instance=video)
        return VideoForm()

    def new_video(self, info, files):
        form = VideoForm(info, files)
        if form.is_valid():
            form.save()
        return form

    def edit_video(self, info, video):
        form = EditVideoForm(info, instance=video)
        if form.is_valid():
            form.save()
        return form


def get_display_video(video):
    return DisplayVideo(video)
