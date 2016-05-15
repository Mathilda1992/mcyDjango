from django.shortcuts import render
from django.http import HttpResponse

from project.models import *

# Create your views here.
def addProject(request):
    project_item = 