from django.shortcuts import render, Http404, redirect
from django.views.generic import View

from .util_home import HomeUtil


class IndexView(View):
    template_name = 'home/index.html'

    def get(self, request):
        user = HomeUtil(request.user)
        if user.is_logged_in():
            return redirect('users:index')
        else:
            return render(request, self.template_name)

    def post(self, request):
        user = HomeUtil(request.user)
        if user.log_user_in(request, request.POST.copy()):
            return redirect('users:index')
        else:
            return render(request, self.template_name, {'error': user.get_error_message()})


def logout_view(request):

    if request.method == 'GET':
        user = HomeUtil(request.user)
        user.log_user_out(request)
        return render(request, 'home/index.html')

    raise Http404






