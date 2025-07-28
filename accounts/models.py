from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import *

import uuid

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    email_confirmed = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        managed = True
        verbose_name ='User'
        verbose_name_plural = 'Users'

class ConfirmationToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email
    