from django.urls import path
from . import views
#for file uploading .......................
from django.conf.urls.static import static
from django.conf import settings
#.....................................
urlpatterns = [
path('', views.index),
path('accounts/',views.Accounts),
path('employeeSearch/',views.EmployeeSearch),
path('salary/',views.Salary),
path('generateSalary/',views.GenerateSalary),

]