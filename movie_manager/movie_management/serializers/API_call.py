from rest_framework import serializers
from ..models import APICall


class APICallSerializer(serializers.ModelSerializer):
    class Meta:
        model = APICall
        fields = ['endpoint', 'timestamp', 'count']
