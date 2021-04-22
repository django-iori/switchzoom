from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

class GuestModel(models.Model):
    name = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    university = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    email = models.EmailField(max_length=240)
    event_date = models.CharField(max_length=20, blank=True)
