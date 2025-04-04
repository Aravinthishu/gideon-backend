from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerialiezer(categories, many=True)
        return Response(serializer.data)
    
class ClientLogoView(APIView):
    def get(self, request):
        clientlogo = ClientLogo.objects.all()
        serializer = ClientLogoSerialiezer(clientlogo, many=True)
        return Response(serializer.data)