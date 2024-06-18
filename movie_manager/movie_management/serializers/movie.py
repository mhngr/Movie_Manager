from rest_framework import serializers
from ..models import Movie, Artist, Director, Actor


class MovieSerializer(serializers.ModelSerializer):

    directors = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())

    class Meta:
        model = Movie
        fields = ['id', 'name', 'production_year', 'directors', 'actors']