from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('list/', ParameterView.as_view({'get': 'list', })),
    path('create/', ParameterView.as_view({'post': 'create', })),
    path('update/<int:pk>/', ParameterView.as_view({'put': 'retrieve', })),
    path('delete/<int:pk>/', ParameterView.as_view({'delete': 'destroy', })),
]
