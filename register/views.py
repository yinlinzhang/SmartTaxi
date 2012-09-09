# Create your views here.

from django.http import HttpResponse
from django.core.exceptions import *

from models import *

def register(request):
    try:
        # json request - {type:[u'driver'], info:{}}
#        usertype = request.GET.get('type')
#        usertype = u'driver'
#        if usertype not in REGISTERHANDLER:
#            raise KeyError("Registration failed: invalid user.")
#        return REGISTERHANDLER[usertype](request) # call register method
        if 'type' not in request.POST:
            return passenger_register(request)
        else:
            return REGISTERHANDLER[request.POST['type']](request)
    except KeyError:
        # json response - {ret:[val], err_msg:["msg"]}
        return HttpResponse("not supported.")

def passenger_register(request):
    try:
        print(request.POST['name'])
        print(request.POST['phonenum'])
        print(request.POST['gender'])
        print(request.POST['password'])

        _name = request.POST['name']
        _phonenum = request.POST['phonenum']
        _gender = request.POST['gender']
        _password = request.POST['password']

        Passenger.objects.get(phonenum = _phonenum)
        return HttpResponse("already existed.")
    except ObjectDoesNotExist:
        passenger = Passenger(name = _name,
            phonenum = _phonenum,
            gender = _gender,
            password = _password,
        )
        passenger.save()
        return HttpResponse("succeeded.")
    except KeyError:
        return HttpResponse("invalid input.")

def driver_register(request):
    return HttpResponse("driver_register")

def taxi_register(request):
    return HttpResponse("taxi_register")

def date(request):
    import datetime
    now = datetime.datetime.now()
    item_list = ['book1', 'book2', 'book3',]
    return HttpResponse("Your request's path: %s, host: %s" % (request.path, request.get_host()))
#    return render_to_response('order.html', {'person_name':'rafael', 'company':'IBM',
#                      'ordered_warranty':False, 'item_list':item_list,
#                      'ship_date':datetime.date(2012, 9, 3),})
    #raise Http404()
    #return HttpResponse(html)

REGISTERHANDLER = {
    u'driver':driver_register,
    u'passenger':passenger_register,
    u'taxi':taxi_register,
    }
