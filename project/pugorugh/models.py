from django.contrib.auth.models import User
from django.db import models

class UserPerf(models.Model):
    user = models.ForeignKey('auth.User')
    age = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    size = models.CharField(max_length=30)


