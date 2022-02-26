from django.urls import path
from django.views.generic.base import View
from rest_framework import views
from .views import *
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import (TokenObtainPairView , TokenRefreshView)
from . import views



urlpatterns = [
    path('phone/', PhoneNumberApi.as_view(), name='register-phone'),
    path('otp/', VerificationApi.as_view() ),
    # path('phone/<str:phone_number>/register/', RegisterApi.as_view(), name='register-user'),
    path('register/', RegisterApi.as_view(), name='register'),
    # path('login/', LoginApi.as_view(), name='log_in'),
    path('user/', UserListView.as_view(), name='all-user'),
    path('user/<str:phone_number>/', ProfileView.as_view(), name='profile'),
    path('user/<str:phone_number>/edit/', EditProfileView.as_view(), name='edit-profile'),
    # path('user/<int:pk>/edit/phone/update/', EditPhoneNumberApiView.as_view(), name='edit-phone'),
    path('login/', LoginApiView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('user/<str:phone_number>/forget/', UpdatePassPhoneView.as_view(), name='forget'),
    path('delete/<int:pk>/' , RejectView.as_view({'delete': 'destroy',}),  name= 'reject-phone'),
]
