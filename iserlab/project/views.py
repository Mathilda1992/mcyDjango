from django.shortcuts import render
from django.http import HttpResponse

from project.models import *

# Create your views here.

def testconn(request):
    return render(request,'testconn/index.html')

def listvm(request):
    return render(request,'testconn/listvm.html')

def listimage(request):
    return render(request,'testconn/listimage.html')

def createvm(request):
    return render(request,'testconn/createvm.html')

