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
from rest_framework.generics import CreateAPIView, ListAPIView ,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny




class ReaportView(viewsets.ViewSet):
    serializer_class = ReportSerializer
    queryset = Reaport.objects.all()
    permission_classes = (IsAuthenticated,)
    
    def allList(self, request,pk=id):
        queryset = Reaport.objects.all
        serializer = ReportSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
    def oneList(self, request,pk=id):
        queryset = Reaport.objects.filter(id=pk)
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def local(self, request,pk=id):
        queryset = Reaport.objects.filter(confirm=False)
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def final(self, request,pk=id):
        queryset = Reaport.objects.filter(confirm=True)
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
        # serializer = ReportSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        Reaport.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
    
    
    
class RejectView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
     
    def destroy(self, request,pk=id):
        queryset = Profile.objects.get(id=pk).delete()
        # if queryset.exist():
        #     return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
        # else: 
        #     return Response("Item has not been FOUND", status=status.HTTP_404_NOT_FOUND)  
        
        
        



class SigneView(CreateAPIView):
    serializer_class = SigneSerializer   
    permission_classes = (IsAuthenticated,)
    
    

class SigneListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Signe.objects.all()
    serializer_class = SigneSerializer
    lookup_field = 'id'