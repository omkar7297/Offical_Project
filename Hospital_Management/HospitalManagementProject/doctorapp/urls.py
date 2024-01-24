from django.urls import path
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings
#...................................
urlpatterns = [
path('', views.index),
path('doctorpage/',views.Doctorpage),
path('ipdpatienprescription/',views.Ipdpatienprescription),
path('ipdprescription/',views.Ipdprescription),
path('opdprescription/',views.Opdprescription),
path('opdpatienprescription/',views.Opdpatienprescription),
]

