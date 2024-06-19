from django.db import models
from django.utils import timezone


class APICall(models.Model):
    endpoint = models.CharField(max_length=300)
    timestamp = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']
