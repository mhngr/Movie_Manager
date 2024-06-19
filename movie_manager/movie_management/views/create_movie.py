from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from ..serializers import MovieSerializer
from ..models import Movie


class CreateMovie(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     name = data.get('name')
    #     production_year = data.get('production_year')
    #     serializer = MovieSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=HTTP_201_CREATED)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
