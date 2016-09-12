from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from database.models import User, Key, UserKeyLink

class MyView(View):
    def get(self, request):
        return render(request, 'keys/index.html', {})
