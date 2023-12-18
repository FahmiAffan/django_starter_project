from django.db import models

# Create your models here.
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password


class UserManager(UserManager):
    def _create_user(self , email , password = None, **extra_fields):
        extra_fields = {"is_staff" : False, "is_superuser": False, **extra_fields}

        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)


        # if not email:
        #     raise ValueError("Users must have an email address")
        # user = CustomUser(email=email, **extra_fields)
        # if password:
        #     user.set_password(password)
        # else:
        #     user.set_unusable_password()

        return user
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email, password=None, **extra_fields):
        # extra_fields = {**extra_fields, "is_staff": True, "is_superuser": True}
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']

        user = self.create_user(email=email, password=password, **extra_fields)
        return user

class CustomUser(AbstractUser):


    # id = models.IntegerField(primary_key = True)
    email = models.EmailField(max_length=255, unique=True,)
    # password = models.CharField(max_length = 200)
    nama_depan = models.CharField(max_length= 200)
    nama_belakang = models.CharField(max_length= 200)
    first_name = None,
    last_name = None,
    # username = models.CharField(max_length=255)
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    nomor = models.CharField(max_length = 200)
    NIK = models.CharField(max_length= 200)
    Unit = models.CharField(max_length=200)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def _str_(self):
        return self.email