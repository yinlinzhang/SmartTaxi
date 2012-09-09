import traceback
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import simplejson
from locationService.core.location import Location
import register.models

__author__ = 'Administrator'

available_passenger = {}

class Passenger_t:
    def __init__(self, phonenum, location):
        self._phonenum = phonenum
        self._location = location

    def set_phonenum(self, phonenum):
        self._phonenum = phonenum

    def get_phonenum(self):
        return self._phonenum

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

def updatePassengerHook(dic):
    pnum = dic['phoneNum']
    if pnum not in available_passenger:
        register.models.verify_passenger_phonenum(pnum)
        available_passenger[pnum] = Passenger_t(pnum, Location(dic['curAddr'], dic['curGeoPoint']))
    else:
        available_passenger[pnum].set_location(Location(dic['curAddr'], dic['curGeoPoint']))
    print "available passenger list: ", repr(available_passenger)

def updatePassenger(request):
    try:
        _jsonobj = request.POST['jsonobj']
        print "jsonobj: ", repr(_jsonobj)
#        simplejson.loads(_jsonobj, object_hook=updatePassengerHook)
        dic = simplejson.loads(_jsonobj)
        updatePassengerHook(dic)
        return HttpResponse(simplejson.dumps({'ret' : 0, 'msg': 'succeeded.'}))
    except KeyError:
        import sys
        print sys.exc_info()[1]
        traceback.print_tb(sys.exc_info()[2])
        return HttpResponse(simplejson.dumps({'ret' : 2, 'msg': 'invalid request.'}))
    except ObjectDoesNotExist:
        import sys
        print sys.exc_info()[1]
        traceback.print_tb(sys.exc_info()[2])
        return HttpResponse(simplejson.dumps({'ret' : 3, 'msg': 'passenger not existed.'}))