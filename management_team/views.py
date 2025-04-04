from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ExpertiseView(APIView):
    def get(self, request):
        expertise = Expertise.objects.all()
        serializer = ExpertiseSerializer(expertise, many=True)
        return Response(serializer.data)
    
class CeosDeskView(APIView):
    def get(self, request):
        ceosdesk = CeosDesk.objects.first()
        serializer = CeosDeskSeiralizers(ceosdesk)
        return Response(serializer.data)