from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    path('list/' ,  ReaportView.as_view({'get':'list',})),
    path('create/' ,  ReaportView.as_view({'post':'create',})),
    path('update/<int:pk>/' ,  ReaportView.as_view({'put':'retrieve',})),
    path('delete/<int:pk>/' ,  ReaportView.as_view({'delete': 'destroy',})),

]