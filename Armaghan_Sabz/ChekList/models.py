from django.db import models
from django.db.models.fields import BooleanField, TextField
from User.models import Profile



class Checklist(models.Model):
    title = models.TextField()
    name = models.CharField(max_length=500)
    signe = models.TextField(null=True)
    function = models.TextField()
    type = models.TextField()
    comment = models.TextField()