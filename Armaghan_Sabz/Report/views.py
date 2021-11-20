from django.shortcuts import render
from django.db.models import QuerySet
from django.views import generic
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.fields import empty
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import viewsets , status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet



class ReaportView(viewsets.ViewSet):
    serializer_class = ReportSerializer
    queryset = Reaport.objects.all()
     
    def list(self, request):
        data = request.GET.get('id')
        if data == empty :
            queryset = Reaport.objects.all
        else:  
            queryset = Reaport.objects.filter(id=data)
        
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=id):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Reaport.objects.get(id=pk).delete()
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    def destroy(self, request,pk=id):
        serializer = ReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Reaport.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
    