import json
from django.http import HttpResponse
from django.http import JsonResponse

### GET ALL schedules
def get_all_schedules(request):
    return None #TODO Return list of all schedules

### GET ALL inventory


### GET all animals


### GET an animal's information
def animal_information(request):
    name = request.GET.get("name")
    
    return JsonResponse({'name':'None'})

### GET all medical records of an animal


### POST appointement
def make_appointment(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    patient_name = body["patientName"]
    owner_name = body["owner"]
    vet_name = body["veterinarian"]
    date = body["appointmentDate"]
    reason = body["operationCategory"]

    #TODO Send information to model.py and return response as a json to frontend
    return JsonResponse({'success':True})

### POST

### POST
