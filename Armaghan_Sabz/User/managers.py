from django.contrib.auth.models import BaseUserManager



class MyUserManager(BaseUserManager):
    def create_superuser(self, phone_number, password, **other_fields):
        # username wa commented
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(phone_number, password, **other_fields)
    # username wa commented

    def create_user(self, phone_number, password, **other_fields):
        # username wa commented
        
        # if not phone_number:
        #     raise ValueError(_('The phone_number must be set'))
        # phone_number = self.normalize_phone_number(phone_number)
        
        # username = phone_number
        User = self.model(phone_number=phone_number, **other_fields)
        # username=username was commented
        
        User.set_password(password)
        User.save()
        return User
    