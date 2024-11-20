from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    instruments = models.ManyToManyField('Instrument', related_name='users')

class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
