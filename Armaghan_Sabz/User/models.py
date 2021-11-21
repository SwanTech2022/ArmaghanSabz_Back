from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.contrib.auth.models import User
from .managers import MyUserManager


# class MyUserManager(BaseUserManager):
#     def create_superuser(self, username, phone_number, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(username, phone_number, password, **other_fields)

#     def create_user(self, username, phone_number, password, **other_fields):

#         username = phone_number
#         User = self.model(username=username,
#                           phone_number=phone_number, **other_fields)
#         User.set_password(password)
#         User.save()
#         return User



class Profile(AbstractBaseUser , PermissionsMixin):
    name = models.CharField(max_length=100 , default=None, null=True)
    family = models.CharField(max_length=100)
    identity_code = models.TextField()
    id_number = models.TextField()
    serial_number = models.TextField()
    address = models.CharField(max_length=500 , unique=True)
    post_code = models.TextField()
    telephone = models.TextField()
    phone_number = models.CharField(unique=True , max_length=13)
    support_phone_number = models.TextField()
    education = models.CharField(max_length=500)
    grade = models.CharField(max_length=500)
    zip_code = models.TextField()
    profession = models.CharField(max_length=300)
    workplace_address = models.CharField(max_length=500)
    job_position = models.CharField(max_length=500)
    workplace_number = models.CharField(max_length=500)
    permission = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    objects = MyUserManager()
    
    def __str__(self):
        return self.phone_number


class OTP(models.Model):
    phone_number = models.IntegerField()
    code = models.IntegerField(null=True)
    
    
    
    
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return str(self.Mobile)