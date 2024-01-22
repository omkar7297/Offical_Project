"""
URL configuration for HospitalManagementProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HospitalManagementProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index),
    path('about_us/',views.About_us),
    path('services/',views.Service),
    path('blog/',views.Blog),
    path('gallary/',views.Gallary),
    path('contact/',views.Contact),
    path('login/',views.Login),
    path('account/',views.Account),
    path('employeesrc/', views.Employeesrc),
    path('salary/', views.Salary),
    path('reception/', views.Reception),
    path('appointment/',views.Appointment),
    path('addmissionform/',views.Addmissionform),
    path('discharge/',views.Discharge),
    path('hospitaladmin/',views.Hospitaladmin),
    path('temporary/',views.Temporary),
    path('registration/',views.Registration),
    path('updateemployee/',views.Updateemployee),
]
 