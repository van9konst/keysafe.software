from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from database.models import User, Key, UserKeyLink

check_history = UserKeyLink.userkeylink_get_data() 
if not check_history['errors'] or check_history['warnings']:
    history = [i for i in check_history['data'] if i.date_returned]

check_taken_keys = UserKeyLink.userkeylink_get_data()
if not check_taken_keys['errors'] or check_taken_keys['warnings']:
    taken = [i for i in check_taken_keys['data'] if not i.date_returned]

check_available_keys = Key.key_get_available()
if not check_available_keys['errors'] or check_available_keys['warnings']:
    available = check_available_keys['data']

class MyView(View):
    def get(self, request):
        return render(request, 'keys/index.html', {'available': available,
                                                   'taken': taken,
                                                   'history':history})
