from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from locationService.views import updatePassenger, requestHandler
import register.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SmartTaxi.views.home', name='home'),
    # url(r'^SmartTaxi/', include('SmartTaxi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', register.views.register),
    url(r'^locationService/$', requestHandler),
)
