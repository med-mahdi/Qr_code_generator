from django.db import models
from .dataFields import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , blank=False , null=False)
    fname = models.CharField(max_length=15, blank=True, null = True)
    lname = models.CharField(max_length=15, blank=True, null = True)
    emailAddress = models.EmailField(max_length=100, blank=False, null = False)
    age = models.IntegerField(default=0, null = False, blank=False)
    gender = models.CharField(max_length=100,choices=genders,default="status")
    status = models.CharField(max_length=50,choices=status,default="status")
    longitude = models.CharField(max_length=30, null=False , blank=False)
    latitude = models.CharField(max_length=30, null=False , blank=False)
    country = models.CharField(max_length=30, null=False , blank=False) 
    city = models.CharField(max_length=50,choices=cities_choice,default="Casablanca")
    bio = models.TextField(max_length=600,blank=True, default="No Bio", null=True)
    date_created = models.DateField(null=True,blank=False,auto_now_add=True)
    date_updated = models.DateField(null=True,blank=False,auto_now=True)
    last_login = models.DateField(null=True,blank=False,auto_now=True)
    # Hobbies For User Profile

    def fullName(self):
        return self.fname + " " + self.lname

    def __str__(self):
        return self.fullName()



class QrCodeModel(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.URLField()
    qr_code_image = models.ImageField(upload_to='qr_codes/')
    
    def __repr__(self):
        return self.name