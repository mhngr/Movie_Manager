from django.db import models


class ApiCall(models.Model):
    endpoint = models.CharField(max_length=300)
    count = models.IntegerField(default=0)
