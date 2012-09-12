# Create your views here.

from django.http import HttpResponse
from django.core.exceptions import *

from models import *

def register(request):
    try:
        # json request - {type:[u'driver'], 'info':{}}
        return REGISTERHANDLER[request.POST['type']](request)
    except KeyError:
        # json response - {ret:[val], err_msg:["msg"]}
        return HttpResponse("not supported.")

def passenger_register(request):
    try:
        Passenger.objects.get(phonenum = request.POST['phonenum'])
        return HttpResponse("passenger already existed.")
    except ObjectDoesNotExist:
        passenger = Passenger(name = request.POST['name'],
            phonenum = request.POST['phonenum'],
            gender = request.POST['gender'],
            password = request.POST['password'],
        )
        passenger.save()
        return HttpResponse("succeeded.")
    except KeyError:
        return HttpResponse("invalid input.")

def driver_register(request):
    try:
        Driver.objects.get(phonenum = request.POST['phonenum'])
        return HttpResponse("driver already existed.")
    except ObjectDoesNotExist:
        driver = Driver(name = request.POST['name'],
            phonenum = request.POST['phonenum'],
            gender = request.POST['gender'],
            password = request.POST['password'],
        )
        driver.save()
        return HttpResponse("succeeded.")
    except KeyError:
        return HttpResponse("invalid input.")

def taxi_register(request):
    return HttpResponse("taxi_register")

REGISTERHANDLER = {
    u'driver':driver_register,
    u'passenger':passenger_register,
    u'taxi':taxi_register,
    }
