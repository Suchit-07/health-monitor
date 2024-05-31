from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name = 'home'),
    path('patient/<int:id>', views.patient, name = 'patient'),
    path('search-patients/', views.search_patients, name = 'search-patients'),
    path('systolic/<int:id>', views.systolic, name = "systolic"),
    path('diastolic/<int:id>', views.diastolic, name = "diastolic"),
    path('heart-rate/<int:id>', views.heartRate, name = "heart-rate"),
    path('blood-oxygen/<int:id>', views.bloodOxygen, name = "blood-oxygen"),
    path('temperature/<int:id>', views.temperature, name = "temperature"),
    path('alarm/<int:id>', views.alarm, name = "alarm"),
    path('add-patient/', views.add_patients, name = 'add-patients'),

]