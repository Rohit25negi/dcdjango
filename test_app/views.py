from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class TestAPI(APIView):
    
    def get(self, request, format=None):
        return Response({"message":" hello world V2!!!"})