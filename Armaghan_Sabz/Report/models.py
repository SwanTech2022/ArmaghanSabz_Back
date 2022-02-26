from django.db import models
from django.db.models.fields import BooleanField, TextField
from User.models import Profile





class Signe(models.Model):
    signe = models.TextField(null=True)



class Reaport(models.Model):
    user_name = models.TextField()
    reciver = models.TextField()
    subject = models.TextField()
    body = models.TextField()
    NotableItem = models.TextField()
    FutureActions = models.TextField()
    singe_rep = models.ForeignKey(Signe ,on_delete=models.CASCADE)
    date = models.TextField()
    time = models.TextField()
    file_name = models.TextField()
    confirm = models.BooleanField()