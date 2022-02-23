from django.db import models
from django.db.models.fields import TextField
from User.models import Profile



class Parameter(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    function = models.TextField()
    engineer_name = models.TextField()
