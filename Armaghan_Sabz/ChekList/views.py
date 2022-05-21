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
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView , RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny





class ChecklistView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChecklistSerializer
    queryset = Checklist.objects.all()

    def list(self, request):
        queryset = Checklist.objects.all()
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
        Checklist.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)



class ContactListView(ListView):
    paginate_by = 2
    model = Checklist
    permission_classes = (IsAuthenticated,)

    def listing(request):
        contact_list = Checklist.objects.all()
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj})
    
    


class SigneView(CreateAPIView):
    serializer_class = SigneSerializer  
    permission_classes = (IsAuthenticated,)
    
    

class SigneListView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Signe.objects.all()
    serializer_class = SigneSerializer
    lookup_field = 'id'    