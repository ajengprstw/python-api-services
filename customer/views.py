from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import customersSerializer
from .models import customers

def index(request):
    return HttpResponse("Hello, Welcome.")

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name' : 'ajeng',
            'address': "pasar minggu",
            'phone':  "08121345678",
            "email": "ajeng@algorit.ma"
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = customersSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
