from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Empregistration, Salaryprocess, Patientsignup,Admissionform, Opdappoientment


curl = settings.CURRENT_URL


def Index(request):
    return render(request, "index.html")

def About_us(request):
    return render(request, "about_us.html", {"curl":curl})

def Service(request):
    return render(request, "services.html", {"curl":curl})

def Blog(request):
    return render(request, "blog.html",{"curl":curl})

def Gallary(request):
    return render(request, "gallery.html", {"curl":curl})

def Contact(request):
    return render(request, "contact_us.html", {"curl":curl})

def Login(request):
    return render(request, "login.html", {"curl":curl})

def Account(request):
    return render(request, "accounts.html", {"curl":curl})

def Employeesrc(request):
    return render(request, "employeesrc.html", {"curl":curl})

def Salary(request):
    return render(request, "salary.html", {"curl":curl})

def Reception(request):
        return render(request, "reception.html",{"curl":curl})

def Appointment(request):
    return render(request,"appointment.html",{"curl":curl})

def Addmissionform(request):
    return render(request, "addmissionform.html",{"curl":curl})

def Discharge(request):
    return render(request,"discharge.html",{"curl":curl})

def Hospitaladmin(request):
    return render(request,"hospitaladmin.html", {'curl':curl})

def Temporary(request):
    return render(request,"temporary.html",{"curl": curl})

def Registration(request):
    return render(request,"registration.html",{"curl":curl})

def Updateemployee(request):
    return render(request, "updateemployee.html",{'curl':curl})