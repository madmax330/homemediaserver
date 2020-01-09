from .forms import NewMessageForm


class BaseUtil:

    def __init__(self):
        self._name = 'Base Util'
        self._form = None
        self._user = None
        self.__errors = []

    def add_error(self, err):
        self.__errors.append(err)

    def get_errors(self):
        return self.__errors

    def get_error_message(self):
        if len(self.__errors) > 0:
            m = ''
            for x in self.__errors:
                m += ' - ' + x + '/n'
            return m
        else:
            return 'No errors.'

    def add_util_errors(self, errs):
        self.__errors.extend(errs)

    def add_form_errors(self):
        for key, value in self._form.errors.items():
            for x in value:
                msg = key + ': ' + x
                self.add_error(msg)

    def new_message(self, msg, code):
        info = {
            'user': self._user.id,
            'message': msg,
            'code': code,
        }
        self._form = NewMessageForm(info)
        if self._form.is_valid():
            self._form.save()
            return True
        self.add_form_errors()
        return False









