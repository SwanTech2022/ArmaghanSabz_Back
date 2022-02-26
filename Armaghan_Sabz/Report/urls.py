from .views import *
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    path('list/' ,  ReaportView.as_view({'get':'allList',})),
    path('single_list/<int:pk>/' ,  ReaportView.as_view({'get':'oneList',})),
     path('local/' ,  ReaportView.as_view({'get':'local',})),
    path('global/' ,  ReaportView.as_view({'get':'final',})),
    path('create/' ,  ReaportView.as_view({'post':'create',})),
    path('update/<int:pk>/' ,  ReaportView.as_view({'put':'retrieve',})),
    path('delete/<int:pk>/' ,  ReaportView.as_view({'delete': 'destroy',})),
    path('createSigne/', SigneView.as_view()),
    path('signe/<int:id>/', SigneListView.as_view()),
]