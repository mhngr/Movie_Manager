from django.db import models
roles = ((0, "actor"), (1, "director"))


class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=20, choices=roles, null=True)

