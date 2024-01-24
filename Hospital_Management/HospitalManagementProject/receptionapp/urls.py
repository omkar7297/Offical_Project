from django.urls import path
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings
#.....................................



urlpatterns = [
path('', views.index),
path('reception/',views.Reception),
path('addmissionform/',views.Addmissionform),
path('discharge/',views.Discharge),
path('ipdpatientsearch/',views.Ipdpatientsearch),
path('ipdprescriptiondetails/',views.Ipdprescriptiondetails),
path('opdpatientsearch/',views.Opdpatientsearch),
path('opdprescriptiondetails/',views.Opdprescriptiondetails),
]



