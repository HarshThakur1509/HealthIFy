from re import M
from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    specialzation = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    fees = models.IntegerField()
    image = models.ImageField( upload_to = "static/", default = "" )
    
    def __str__(self) :
        return self.name
    
class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    disc = models.TextField(blank=True)
    
   