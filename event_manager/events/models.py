from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

class Meta:
    ordering = ['start_datetime']
