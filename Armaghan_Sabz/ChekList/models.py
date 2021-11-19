from django.db import models
from django.db.models.fields import BooleanField, TextField
from User.models import Profile



class Checklist(models.Model):
    title = models.TextField()
    subtitle = models.CharField(max_length=500)
    content = models.CharField(max_length=500)
    time = models.TextField()
    date = models.TextField()
    date2 = models.TextField()
    category = models.CharField(max_length=500 , null=True)
    comment = models.CharField(max_length=500 , null=True)
    kind = models.IntegerField()
    value = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file_name = models.TextField()
    confirm = models.BooleanField()
    user_id = models.IntegerField()
    signe = models.TextField(null=True)