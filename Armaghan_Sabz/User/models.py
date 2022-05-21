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
    name = models.TextField()
    family = models.TextField()
    id_number = models.TextField()
    serial_number = models.TextField()
    address = models.TextField()
    telephone = models.TextField(null=True, blank=True)
    phone_number = models.TextField(unique=True, max_length=11, null=True, blank=True)
    education = models.TextField()
    grade = models.TextField()
    support_phone_number = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    profession = models.TextField(blank=True, null=True)
    workplace_address = models.TextField(blank=True, null=True)
    job_position = models.TextField(blank=True, null=True)
    workplace_number = models.TextField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone_number'
    objects = MyUserManager()
    USERNAME_FIELD = 'phone_number'
    objects = MyUserManager()
    
    def __str__(self):
        return self.phone_number





class OTP(models.Model):
    phone_number = models.TextField(max_length=11)
    code = models.IntegerField(null=True)
    
    

    
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return str(self.Mobile)