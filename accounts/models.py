from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import CustomUserManager
import uuid

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_confirmed_email = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class ConfirmationToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(CustomUser, related_name='confirmation', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', null=True)
    phone = models.BigIntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
