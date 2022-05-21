from django.db import models
from django.db.models.fields import BooleanField, TextField
from User.models import Profile



class Signe(models.Model):
    signe = models.TextField(null=True)
    

class Checklist(models.Model):
    title = models.TextField()
    name = models.CharField(max_length=500)
    singe_chek = models.ForeignKey(Signe ,on_delete=models.CASCADE, blank=True, null=True)
    functions = models.TextField()
    types = models.TextField()
    comment = models.TextField()