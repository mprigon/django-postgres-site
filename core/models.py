from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    skills = models.TextField(max_length=256)
    mobile_phone = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.username
