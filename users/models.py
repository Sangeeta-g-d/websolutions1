from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.


class NewUser(AbstractUser):
    description = models.CharField(max_length=600, default='project requirement')
