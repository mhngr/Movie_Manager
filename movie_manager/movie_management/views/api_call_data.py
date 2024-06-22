from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import ApiCall
from ..serializers import APICallSerializer


class APICallData(APIView):
    def get(self, request):
        api_calls = ApiCall.objects.all().order_by('-timestamp')
        serializer = APICallSerializer(api_calls, many=True)
        return Response(serializer.data)
