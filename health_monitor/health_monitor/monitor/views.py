from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import logging
import random

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render(request, 'health_monitor.html')

def systolic(request):
    systolic = random.randint(100, 140)
    return HttpResponse(str(systolic) + ' mmHg')

def diastolic(request):
    diastolic = random.randint(60, 90)
    return HttpResponse(str(diastolic) + ' mmHg')

def heartRate(request):
    heartRate = random.randint(70, 140)
    return HttpResponse(str(heartRate) + ' BPM')

def bloodOxygen(request):
    bloodOxygen = random.randint(94, 100)
    return HttpResponse(str(bloodOxygen) + ' %')