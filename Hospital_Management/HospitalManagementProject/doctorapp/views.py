# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from HospitalManagementProject import settings
from HospitalManagementProject import models
from django.db.models.expressions import RawSQL
#for file uploading
from django.core.files.storage import FileSystemStorage
#for logout
from django.contrib.auth import logout
#for display image
from django.conf import settings
media_url=settings.MEDIA_URL
# Create your views here.
curl = settings.CURRENT_URL
import time
import datetime
#django rest framework
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("<h1>Welcome to Doctor Admin App</h1>")


def Doctorpage(request):
    return render(request,'doctorpage.html',{'curl':curl})

def Ipdpatienprescription(request):
    return render(request,'ipdpatienprescription.html',{'curl':curl})

def Ipdprescription(request):
    return render(request,'ipdprescription.html',{'curl':curl})

def Opdprescription(request):
    return render(request,'opdprescription.html',{'curl':curl})

def Opdpatienprescription(request):
    return render(request,'opdpatienprescription.html',{'curl':curl})



