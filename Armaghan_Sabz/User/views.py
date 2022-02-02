from django.db.models import fields
from django.shortcuts import render
from django.db import models
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import (EditProfileUserSerializer, LoginSerializer, OtpSerializer, UpdatePassSerializer,
    # VerificationForgetSerializer,
                          ForgetPassSerializer,
                          RegisterSerializer,
                          UserSerializer,
                          CustomJWTSerializer,
                          VerificationSerializer,
    # UpdatePhoneNumberSerializer,
                          )
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import make_verification_code
from rest_framework import status, request, viewsets
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# for making code and send sms
class PhoneNumberApi(CreateAPIView):
    serializer_class = OtpSerializer


# for sending SMS and start registering
# @api_view(['GET', 'POST'])
# def verificationApi(request):
#     data = {
#         'phone_number': request.POST.get('phone_number', False),
#         'code': request.data['code'],
#     }

#     ser = VerificationSerializer(data=data)
#     if ser.is_valid():
#         query = OTP.objects.filter(phone_number=request.POST.get('phone_number', False), code=request.POST.get('code'))
#         if query.exists():
#             return Response(status.HTTP_200_OK)
#         else:
#             return Response(status.HTTP_404_NOT_FOUND)
class VerificationApi(CreateAPIView):
    serializer_class =  VerificationSerializer


class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginApi(ListAPIView):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'phone_number': user.phone_number
        })

    serializer_class = LoginSerializer
    queryset = Profile.objects.all()


class UserListView(ListAPIView):
    # permission_classes = (IsAdminUser,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


class ProfileView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


class EditProfileView(UpdateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = EditProfileUserSerializer
    lookup_field = 'phone_number'


# class EditPhoneNumberApiView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdatePhoneNumberSerializer
#     queryset = Profile.objects.all()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


# forget pass with phone/email
class ForgetPassView(CreateAPIView):
    serializer_class = ForgetPassSerializer


# # for verify code
# class VerificationForgetApi(CreateAPIView):
#     serializer_class =  VerificationForgetSerializer


# change pass with phone_number
class UpdatePassPhoneApiView(UpdateAPIView):
    serializer_class = UpdatePassSerializer
    lookup_field = 'phone_number'

    def get_queryset(self):
        query = (str(self.request).split('/'))
        return Profile.objects.filter(phone_number=str(query[3]))


class RejectView(viewsets.ViewSet):

    def destroy(self, request, pk=id):
        queryset = Profile.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)

        # if queryset.exist():
        #     return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
        # else:
        #     return Response("Item has not been FOUND", status=status.HTTP_404_NOT_FOUND)
