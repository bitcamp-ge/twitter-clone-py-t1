from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    bio = models.CharField(max_length=128, null=True)
    
    def __str__(self):
        return self.username
