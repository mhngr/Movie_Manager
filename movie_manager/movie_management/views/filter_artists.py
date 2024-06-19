from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Artist
from ..serializers import ArtistSerializer


class FilterArtists(APIView):
    def get(self, request):
        filter_by = request.query_params.get('filter')
        queryset = Artist.objects.all()
        if filter_by == 'actors':
            queryset = queryset.filter(actor__isnull=False).distinct()
        elif filter_by == 'directors':
            queryset = queryset.filter(director__isnull=False).distinct()
        serializer = ArtistSerializer(queryset, many=True)
        return Response(serializer.data)


