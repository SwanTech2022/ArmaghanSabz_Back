from django.shortcuts import render
from django.db.models import QuerySet
from django.views import generic
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import viewsets , status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import GenericViewSet



class ChecklistView(viewsets.ViewSet):
    serializer_class = ChecklistSerializer
    queryset = Checklist.objects.all()
     
    def list(self, request):
        queryset = Checklist.objects.filter(kind = request.GET.get('kind', False), confirm = request.GET.get('confirm', False))
        serializer = ChecklistSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = ChecklistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=id):
        serializer = ChecklistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Checklist.objects.get(id=pk).delete()
        serializer = ChecklistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    
    def destroy(self, request,pk=id):
        serializer = ChecklistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Checklist.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
    