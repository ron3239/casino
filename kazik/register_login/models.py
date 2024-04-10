from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Player(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    token = models.IntegerField(default=20)

    def __str__(self) -> str:
        return self.username
    




