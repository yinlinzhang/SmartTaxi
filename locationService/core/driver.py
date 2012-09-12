import traceback
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.utils import simplejson
from locationService.core.location import Location
import register.models

__author__ = 'Administrator'

available_drivers = {}

class Driver_t:
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

def updateDriverHook(dic):
    pnum = dic['phoneNum']
    if pnum not in available_drivers:
        register.models.verify_driver_phonenum(pnum)
        available_drivers[pnum] = Driver_t(pnum, Location(dic['curAddr'], dic['curGeoPoint']))
    else:
        available_drivers[pnum].set_location(Location(dic['curAddr'], dic['curGeoPoint']))
    print "available driver list: ", repr(available_drivers)

def updateDriver(request):
    try:
        _jsonobj = request.POST['jsonobj']
        print "jsonobj: ", repr(_jsonobj)
        #        simplejson.loads(_jsonobj, object_hook=updateDriverHook)
        dic = simplejson.loads(_jsonobj)
        updateDriverHook(dic)
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
        return HttpResponse(simplejson.dumps({'ret' : 3, 'msg': 'driver not existed.'}))
