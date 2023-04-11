from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ID_Number = models.PositiveIntegerField(unique=True, null=True)
    email = models.EmailField( null = True)
    



