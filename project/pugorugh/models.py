from django.contrib.auth.models import User
from django.db import models

class UserPerf(models.Model):
    user = models.ForeignKey('auth.User')
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    size = models.CharField(max_length=30)

class Dog(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=225)
    breed = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    size = models.CharField(max_length=2)
