from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.


"""
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
"""

class Passenger(models.Model):
    phonenum = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64, null=False)
    gender = models.BooleanField(default=True)
    password = models.CharField(max_length=64, null=False)

class Taxi(models.Model):
    taxiid = models.CharField(max_length=64, primary_key=True)
    vendor = models.CharField(max_length=128, null=False)

class Driver(models.Model):
    phonenum = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64, null=False)
    gender = models.BooleanField(default=True)
    password = models.CharField(max_length=64, null=False)
#    taxi = models.OneToOneField(Taxi)

def verify_passenger_phonenum(pnum):
    if pnum not in [ o.phonenum for o in Passenger.objects.all()]:
        raise ObjectDoesNotExist()

def verify_driver_phonenum(pnum):
    if pnum not in [ o.phonenum for o in Driver.objects.all()]:
        raise ObjectDoesNotExist()