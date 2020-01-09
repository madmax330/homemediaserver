from django.contrib.auth import authenticate, login, logout

from .base_util import BaseUtil


class HomeUtil(BaseUtil):

    def __init__(self, user):
        super(HomeUtil, self).__init__()
        self._name = 'User Util'
        self._user = user

    #
    #   USER LOGIN FUNCTIONS
    #

    def log_user_in(self, request, info):
        self._user = authenticate(username='coulibaly', password=info['password'])
        if self._user is not None:
            if self._user.is_active:
                login(request, self._user)
                return True
            else:
                self.add_error('User not active.')
                return False
        else:
            self.add_error('Invalid login credentials.')
            return False

    def log_user_out(self, request):
        logout(request)

    def is_logged_in(self):
        return self._user.is_authenticated

    #
    #   User Functions
    #

