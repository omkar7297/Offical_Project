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
    return HttpResponse("<h1>Welcome to Reception App</h1>")

def Reception(request):
    return render(request,'reception.html',{'curl':curl})

def Addmissionform(request):
    return render(request,'addmissionform.html',{'curl':curl})

def Discharge(request):
    return render(request,'discharge.html',{'curl':curl})

def Ipdpatientsearch(request):
    return render(request,'ipdpatientsearch.html',{'curl':curl})

def Ipdprescriptiondetails(request):
    return render(request,'ipdprescriptiondetails.html',{'curl':curl})

def Opdpatientsearch(request):
    return render(request,'opdpatientsearch.html',{'curl':curl})

def Opdprescriptiondetails(request):
    return render(request,'opdprescriptiondetails.html',{'curl':curl})


