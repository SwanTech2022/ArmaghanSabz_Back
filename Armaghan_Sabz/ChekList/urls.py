from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    path('List/' ,  ChecklistView.as_view({'get':'list',})),
    path('Create/' ,  ChecklistView.as_view({'post':'create',})),
    path('Update//<int:pk>/' ,  ChecklistView.as_view({'put':'retrieve',})),
    path('Delete/<int:pk>/' ,  ChecklistView.as_view({'delete': 'destroy',})),


]
