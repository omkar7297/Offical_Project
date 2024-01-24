from django.urls import path
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings
#.....................................
urlpatterns = [
path('', views.index),
path('Hospitaladmin/',views.Hospitaladmin),
path('hospitaladministrator/',views.Hospitaladministrator),
path('employeesrc/',views.Employeesrc),
path('registration/',views.Registration),
path('updateemployee/',views.Updateemployee),
path('equipements/',views.Equipements),

]