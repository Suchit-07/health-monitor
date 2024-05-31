from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import logging
import os
import requests

logger = logging.getLogger(__name__)

def apiGet(url):
    headers = {
        'Authorization': f'Bearer {os.getenv("API_KEY")}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed API request. Status code: {response.status_code}, URL: {url}")
        return None

def search(request):
    return render(request, 'search.html')

def search_patients(request):
    url = "https://health-api.hscc-atlanta.com/v3/patients"
    response = apiGet(url)
    
    if response:
        name = request.GET.get('query', '')
        if not name:
            return render(request, 'patients.html', {'patients': response['patients']})

        searchResults = [x for x in response["patients"] if name.lower() in x['name'].lower()]
        
        return render(request, 'patients.html', {'patients': searchResults})
    else:
        return HttpResponse("Some error occurred, try again")

def patient(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}"
    response = apiGet(url)

    if response:
        return render(request, 'health_monitor.html', {"patient": response, "id": id})
    else:
        return HttpResponse("Some error occurred, try again")

def systolic(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/bp"
    response = apiGet(url)

    if response:
        if response.get("alarm"):
            return HttpResponse(f"<h5 class='card-text alarm'>{response['value']['sys']} mmHg</h5>")
        else:
            return HttpResponse(f"<h5 class='card-text'>{response['value']['sys']} mmHg</h5>")
    else:
        return HttpResponse("Some error occurred, try again")

def diastolic(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/bp"
    response = apiGet(url)

    if response:
        if response.get("alarm"):
            return HttpResponse(f"<h5 class='card-text alarm'>{response['value']['dia']} mmHg</h5>")
        else:
            return HttpResponse(f"<h5 class='card-text'>{response['value']['dia']} mmHg</h5>")
    else:
        return HttpResponse("Some error occurred, try again")

def heartRate(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/hr"
    response = apiGet(url)

    if response:
        if response.get("alarm"):
            return HttpResponse(f"<h5 class='card-text alarm'>{response['value']} BPM</h5>")
        else:
            return HttpResponse(f"<h5 class='card-text'>{response['value']} BPM</h5>")
    else:
        return HttpResponse("Some error occurred, try again")

def bloodOxygen(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/box"
    response = apiGet(url)

    if response:
        if response.get("alarm"):
            return HttpResponse(f"<h5 class='card-text alarm'>{response['value']} %</h5>")
        else:
            return HttpResponse(f"<h5 class='card-text'>{response['value']} %</h5>")
    else:
        return HttpResponse("Some error occurred, try again")

def temperature(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/temp"
    response = apiGet(url)

    if response:
        if response.get("alarm"):
            return HttpResponse(f"<h5 class='card-text alarm'>{response['value']} °F</h5>")
        else:
            return HttpResponse(f"<h5 class='card-text'>{response['value']} °F</h5>")
    else:
        return HttpResponse("Some error occurred, try again")

def alarm(request, id):
    url = f"https://health-api.hscc-atlanta.com/v3/patients/{id}/all"
    response = apiGet(url)
    if response:
        alarm = 0
        if response['hr']['alarm'] == True:
            alarm += 1
        if response['box']['alarm'] == True:
            alarm += 1
        if response['temp']['alarm'] == True:
            alarm += 1
        if response['bp']['alarm'] == True:
            alarm += 1
        if(alarm >= 2):
            return HttpResponse('<script>document.body.classList.add("alarm-active");</script>')
        else:
            return HttpResponse('<script>document.body.classList.remove("alarm-active");</script>')

def add_patients(request):
    return render(request, 'patient-add.html')