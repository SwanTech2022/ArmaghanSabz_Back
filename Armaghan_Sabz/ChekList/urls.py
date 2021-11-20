from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    path('list/' ,  ChecklistView.as_view({'get':'list',})),
    path('create/' ,  ChecklistView.as_view({'post':'create',})),
    path('update/<int:pk>/' ,  ChecklistView.as_view({'put':'retrieve',})),
    path('delete/<int:pk>/' ,  ChecklistView.as_view({'delete': 'destroy',})),


]
