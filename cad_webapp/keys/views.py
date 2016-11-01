from django.shortcuts import render
from django.views.generic import View
from models import Key, UserKeyLink


class MyView(View):

    def get(self, request, available=None, taken=None, history=None):

        check_history = UserKeyLink.get_all_operations()
        if not check_history['errors'] or check_history['warnings']:
            history = [i for i in check_history['data'] if i.date_returned]

        check_taken_keys = UserKeyLink.get_all_operations()
        if not check_taken_keys['errors'] or check_taken_keys['warnings']:
            taken = [i for i in check_taken_keys['data'] if not i.date_returned]

        check_available_keys = Key.get_available_keys()
        if not check_available_keys['errors'] or check_available_keys['warnings']:
            available = check_available_keys['data']
        return render(request, 'keys/index.html', {'available': available,
                                                   'taken': taken,
                                                   'history': history})