from ..models import APICall
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.request import Request


class APICallTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: Request):
        endpoint = request.path_info
        try:
            apicall = APICall.objects.get(endpoint=endpoint)
        except APICall.DoesNotExist:
            apicall = APICall(endpoint=endpoint)
        apicall.count += 1
        apicall.save()
        response = self.get_response(request)
        return response
