from rest_framework import serializers
from ..models import ApiCall


class APICallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiCall
        fields = ['endpoint', 'timestamp', 'count']
