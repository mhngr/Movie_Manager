from rest_framework import serializers


class ExtensionSerializer(serializers.Serializer):
    name = serializers.CharField()
    version = serializers.CharField()
    author = serializers.CharField()
    summary = serializers.CharField()
