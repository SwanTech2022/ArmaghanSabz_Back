"""Armaghan_Sabz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from User import urls as User_urls 
from ChekList import urls as ChekList_urlss
from Report import urls as Report_urls
from Parameter import urls as Parameter_urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('cheklist/', include('ChekList.urls')),
    path('report/', include('Report.urls')),
    path('parameter/', include('Parameter.urls')),
]


urlpatterns += staticfiles_urlpatterns()