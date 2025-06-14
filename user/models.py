from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, phonenumber=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')

        # Require phone number only for non-superusers
        if not phonenumber and not extra_fields.get('is_superuser'):
            raise ValueError('The Phone Number must be set')

        user = self.model(username=username, phonenumber=phonenumber, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

# Create your models here.
class User(AbstractUser):
    phonenumber = models.CharField(max_length=10,unique=True, null=True, blank=True)
    
    name = models.CharField(max_length=255, default="DefaultName")
    email = models.EmailField(blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'  
    REQUIRED_FIELDS = [] 
    first_name = None
    last_name = None

    def __str__(self):
        return self.username