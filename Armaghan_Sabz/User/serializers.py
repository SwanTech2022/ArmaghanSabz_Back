from enum import unique
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models import fields, query
from rest_framework import permissions, serializers, status
from rest_framework.fields import empty
from rest_framework.response import Response
from .models import OTP, Profile
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import make_verification_code, make_forget_code
from random import randint
from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation





# class PhoneNumberSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=11)

#     def create(self, validated_data):
#         code = str(randint(10000,99999))
#         if len(validated_data['phone']) == 11 :
#             return validated_data

#         return {'phone': 'your phone number wrong'}


# class OtpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OTP
#         fields = ('phone_number',)

#     def create(self, validated_data):
#         obj = super().create(validated_data)
#         obj.code = str(randint(10000, 99999))
#         obj.save()
#         make_verification_code(validated_data['phone_number'], obj.code)
#         return obj

#     # check sms code with entiry code for login


# class VerificationSerializer(serializers.Serializer):
#     phone = serializers.CharField(max_length=11)
#     code = serializers.CharField(max_length=5)
    
    
    
#     class Meta:
#         model = OTP
#         fields = '__all__'

#     def verify(self, validate_data):
#         obj = super().create(validate_data)



#     def create(self, validated_data):
#         phone = validated_data['phone']
#         code = validated_data['code']
#         query = OTP.objects.filter(phone_number = phone , code = code)
        

#         if code == 'code expierd':
#             return {'phone':validated_data['phone'], 'code': 'code expierd time'}

#         elif code == validated_data['code']:
#             return validated_data
                

#         return {'phone':validated_data['phone'], 'code': 'code is not correct'}
    
    
    


class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ('phone_number',)
    usersData=[]
    
    def saveUsersCodes(self , phNum,code):
        OtpSerializer.usersData.append((phNum,code))
            
    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.code = str(randint(10000, 99999))
        obj.save()
        make_verification_code(validated_data['phone_number'], obj.code)
        self.saveUsersCodes(validated_data['phone_number'], obj.code)
        return obj

    # check sms code with entiry code for login



class VerificationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=5)
   
    
    class Meta:
        model = OTP
        fields = '__all__'

    def verify(self, validate_data):
        obj = super().create(validate_data)

    
    def create(self, validated_data):
        phone = validated_data['phone']
        code = validated_data['code']
        query = OTP.objects.filter(phone_number = phone , code = code)


        for i in OtpSerializer.usersData:
            if i == (phone,code):
                OtpSerializer.usersData.remove(i)
                return {'phone':validated_data['phone'], 'code': 'code is correct'}
        
        return {'phone':validated_data['phone'], 'code': 'code incorrect'}

    
    
    
        


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'name': {'required': True},
            'family': {'required': True},
            'phone_number': {'required': True},
            'telephone': {'required': True},
            'id_number': {'required': True},
            'serial_number': {'required': True},
            'address': {'required': True},
            'education': {'required': True},
            'grade': {'required': True},
        }

    def create(self, validated_data):
        user = Profile.objects.create(
            name=validated_data['name'],
            family=validated_data['family'],
            password=make_password(validated_data['password']),
            phone_number=validated_data['phone_number'],
            id_number=validated_data['id_number'],
            serial_number=validated_data['serial_number'],
            address=validated_data['address'],
            education=validated_data['education'],
            grade=validated_data['grade'],
            support_phone_number=validated_data['support_phone_number'],
            telephone=validated_data['telephone'],
            zip_code=validated_data['zip_code'],
            profession=validated_data['profession'],
            workplace_address=validated_data['workplace_address'],
            job_position=validated_data['job_position'],
            workplace_number=validated_data['workplace_number'],
            is_staff = validated_data['is_staff'],
            is_active = validated_data['is_active'],
            is_superuser = validated_data['is_superuser']
            )
            
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     def validate(self, validated_data):
#         if Profile.objects.filter(phone=validated_data['phone_number']):
#             # ,Permission=True
#             pass
#         return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }


class EditProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ('password','phone_number')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # you can login with email and phone_number


class CustomJWTSerializer(TokenObtainPairSerializer):
    username_field = 'phone_number'
    def validate(self, attrs):
        credentials = {
            'phone_number': '',
            'password': attrs.get("password")
        }
        user_obj = Profile.objects.filter(phone_number=attrs.get("phone_number")).first()

        if user_obj:
            credentials['phone_number'] = user_obj.phone_number
            
        data = super().validate(credentials)
        data['is_staff'] = self.user.is_staff
        data['is_active'] = self.user.is_active
        data['is_superuser'] = self.user.is_superuser
        

        return data


# forget pass send code with phone/email
class ForgetPassSerializer(serializers.Serializer):
        model = Profile
        password = serializers.CharField(required=True)
        confirm_password = serializers.CharField(required=True)
    
# check sms code with entiry code for login
# class VerificationForgetSerializer(serializers.Serializer):
#     phone = serializers.IntegerField()
#     code = serializers.CharField(max_length=5)

#     def create(self, validated_data):
#         data = verification(validated_data['phone'])

#         if data == 'code expierd':
#             return {'phone':validated_data['phone'], 'code': 'code expierd time'}

#         elif data == validated_data['code']:
#             return validated_data

#         return {'phone':validated_data['phone'], 'code': 'code is not correct'}


# update password after get code
class UpdatePassSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = Profile
        fields = ['password', 'confirm_password']

    def update(self, instance, validated_data):
        if validated_data['password'] == validated_data['confirm_password']:
            validated_data = {'password': make_password(validated_data['password']),
                              'confirm_password': validated_data['confirm_password']}

            return super().update(instance, validated_data)

        return {'password': validated_data['password'], 'confirm_password': 'password dose not match !'}
  