# Create your views here.
import traceback

from django.http import HttpResponse
from django.utils import simplejson
from locationService.core.passenger import updatePassenger

def requestHandler(request):
    try:
        return request.POST['target'](request)
    except KeyError:
        import sys
        print sys.exc_info()[1]
        traceback.print_tb(sys.exc_info()[2])
        return HttpResponse(simplejson.dumps({'ret' : 1, 'msg': 'unknown request.'}))
    except Exception:
        import sys
        print sys.exc_info()[1]
        traceback.print_tb(sys.exc_info()[2])
        return HttpResponse(simplejson.dumps({'ret' : 16, 'msg': 'unknown error.'}))

HANDLER_MAP = {
    'updatePassenger' : updatePassenger,
#    'updatePassenger' : updatePassenger,
    }