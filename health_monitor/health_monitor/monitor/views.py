from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import logging
import random

logger = logging.getLogger(__name__)

# Create your views here.
def search(request):
    return render(request, 'search.html')

def search_patients(request):
    url = "https://health-api.hscc-atlanta.com/v2/patients"
    response = requests.get(url)
    
    if(response.status_code == 200):
        response = response.json()
        name = request.GET.get('query', '')
        if(not name):
            return render(request, 'patients.html', {'patients': response['patients']})

        searchResults = []

        for x in response["patients"]:
            if name.lower() in x['name'].lower():
                searchResults.append(x)
        
        return render(request, 'patients.html', {'patients': searchResults})
    else:
        return HttpResponse("Some error occured, try again")

    
def patient(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id)
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()
        return render(request, 'health_monitor.html', {"patient": response, "id": id})
    else:
        return HttpResponse("Some error occured, try again")

def systolic(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id) +"/bp"
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()

        return HttpResponse(str(response['value']['sys']) + ' mmHg')
    else:
        return HttpResponse("Some error occured, try again")

def diastolic(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id) +"/bp"
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()

        return HttpResponse(str(response['value']['dia']) + ' mmHg')
    else:
        return HttpResponse("Some error occured, try again")

def heartRate(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id) +"/hr"
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()

        return HttpResponse(str(response['value']) + ' BPM')
    else:
        return HttpResponse("Some error occured, try again")

def bloodOxygen(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id) +"/box"
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()

        return HttpResponse(str(response['value']) + ' %')
    else:
        return HttpResponse("Some error occured, try again")


def temperature(request, id):
    url = "https://health-api.hscc-atlanta.com/v2/patient/" + str(id) +"/temp"
    response = requests.get(url)

    if(response.status_code == 200):
        response = response.json()

        return HttpResponse(str(response['value']) + ' °F')
    else:
        return HttpResponse("Some error occured, try again")