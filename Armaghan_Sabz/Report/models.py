from django.db import models
from django.db.models.fields import BooleanField, TextField
from User.models import Profile



class Reaport(models.Model):
    user_name = models.TextField()
    reciver = models.TextField()
    subject = models.TextField()
    NotableItem = models.TextField()
    FutureActions = models.TextField()
    signe = models.TextField()
    date = models.TextField()
    time = models.TextField()
    file_name = models.TextField()
    confirm = models.BooleanField()