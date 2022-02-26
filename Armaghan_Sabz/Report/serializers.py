from rest_framework import serializers
from django.db.models import fields
from .models import *



class ReportSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Reaport
      
      
      
class SigneSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Signe      