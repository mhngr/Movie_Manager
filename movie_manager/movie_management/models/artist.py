from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
