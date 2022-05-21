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
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny




class ParameterView(viewsets.ViewSet):
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Parameter.objects.all()
        serializer = ParameterSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ParameterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=id):
        serializer = ParameterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Parameter.objects.get(id=pk).delete()
        serializer = ParameterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



    def destroy(self, request,pk=id):
        # serializer = ParameterSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        Parameter.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)



class ContactListView(ListView):
    paginate_by = 2
    model = Parameter
    permission_classes = (IsAuthenticated,)

    def listing(request):
        contact_list = Parameter.objects.all()
        paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'list.html', {'page_obj': page_obj})