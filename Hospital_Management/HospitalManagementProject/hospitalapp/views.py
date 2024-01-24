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
# from rest_framework.parsers import JSONParser
# from.serializers import UserSerializer

def index(request):
    return HttpResponse("<h1>Welcome to Hospital Administrator App!!</h1>")

def Hospitaladmin(request):
    return HttpResponse("<h1>Welcome to Hospital Administrator App Page !!</h1>")

def Hospitaladministrator(request):
    return render(request,"hospitaladministrator.html",{'curl':curl})

def Employeesrc(request):
    return render(request,"employeesrc.html",{'curl':curl})

def Registration(request):
    return render(request,"registration.html",{'curl':curl})

def Updateemployee(request):
    return render(request,"updateemployee.html",{'curl':curl})

def Equipements(request):
    return render(request,"equipements.html",{'curl':curl})
