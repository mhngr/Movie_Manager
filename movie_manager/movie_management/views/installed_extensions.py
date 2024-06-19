from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ExtensionSerializer


class InstalledExtensions(APIView):
    def get(self, request):
        extensions = connection.get_installed_extensions()
        serializer = ExtensionSerializer(extensions, many=True)
        serialized_extensions = serializer.data
        return Response(serialized_extensions)
