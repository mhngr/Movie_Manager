from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..serializers import MovieSerializer
from ..models import Movie


class RegisterMovie(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        production_year = data.get('production_year')
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
