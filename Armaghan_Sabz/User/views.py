from django.db.models import fields
from django.shortcuts import render
from django.db import models
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import (EditProfileUserSerializer, OtpSerializer, UpdatePassSerializer,
    # VerificationForgetSerializer,
                          ForgetPassSerializer,
                          RegisterSerializer,
                          UserSerializer,
                          CustomJWTSerializer,
                          VerificationSerializer,
    # UpdatePhoneNumberSerializer,
                          )
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import make_verification_code
from rest_framework import status, request, viewsets
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404




# for making code and send sms
class PhoneNumberApi(CreateAPIView):
    serializer_class = OtpSerializer
    permission_classes = [AllowAny]


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
    permission_classes = [AllowAny]
    


class RegisterApi(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# class LoginApiView(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                           context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'phone_number': user.phone_number
#         })


class UserListView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


class ProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'phone_number'


class EditProfileView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = EditProfileUserSerializer
    lookup_field = 'phone_number'
    
    def update(self, request, phone_number):
        datas = get_object_or_404(self.queryset, phone_number=phone_number)
        ser = self.serializer_class(data=self.request.data, instance=datas)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)


# class EditPhoneNumberApiView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UpdatePhoneNumberSerializer
#     queryset = Profile.objects.all()


class LoginApiView(TokenObtainPairView):
     serializer_class = CustomJWTSerializer
     permission_classes = [AllowAny]


# forget pass with phone
class ForgetPassView(UpdateAPIView):
    serializer_class = ForgetPassSerializer
    permission_classes = [AllowAny]


# # for verify code
# class VerificationForgetApi(CreateAPIView):
#     serializer_class =  VerificationForgetSerializer


# change pass with phone_number

class UpdatePassPhoneView(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ForgetPassSerializer
    model = Profile
    
    def update(self, request, *args, **kwargs):
        obj = Profile.objects.get(phone_number=self.kwargs["phone_number"])
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if serializer.data.get("password")!=serializer.data.get("confirm_password"):
                return Response({"confirm_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
            obj.set_password(serializer.data.get("password"))
            obj.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                

# class UpdatePassPhoneView(viewsets.ViewSet):
    
#     def update(self, request, pk):
#         user = Profile.objects.get(phone_number=pk)
#         user.set_password(request.data["password"])
#         user.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
        

class RejectView(viewsets.ViewSet):
    permission_classes = (IsAdminUser,)

    def destroy(self, request, pk=id):
        queryset = Profile.objects.get(id=pk).delete()
        return Response("Item has been deleted successfully", status=status.HTTP_204_NO_CONTENT)
