from django.shortcuts import render
from django.http import HttpResponse

import sys
sys.path.append("..") # Adds higher directory to python modules path.

from database.models import User, Key, UserKeyLink

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
