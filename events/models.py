from django.db import models
from django.contrib.auth.models import User

class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Musician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instrument = models.ManyToManyField(Instrument, related_name="musicians")

    def __str__(self):
        return self.user.username
