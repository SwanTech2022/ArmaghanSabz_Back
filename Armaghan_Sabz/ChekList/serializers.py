from rest_framework import serializers
from django.db.models import fields
from .models import *



class ChecklistSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Checklist