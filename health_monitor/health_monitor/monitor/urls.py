from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('systolic/', views.systolic, name = "systolic"),
    path('diastolic/', views.diastolic, name = "diastolic"),
    path('heart-rate/', views.heartRate, name = "heart-rate"),
    path('blood-oxygen/', views.bloodOxygen, name = "blood-oxygen"),

]