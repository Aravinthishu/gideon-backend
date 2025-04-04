from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class WhoWeAreSectionView(APIView):
    def get(self, request):
        company_overview = WhoWeAreSection.objects.all()
        serializer = WhoWeAreSectionSerializer(company_overview, many=True)
        return Response(serializer.data)
    
class OurMissionVisionView(APIView):
    def get(self, request):
        company_overview = OurMissionVision.objects.all()
        serializer = OurMissionVisionSerializer(company_overview, many=True)
        return Response(serializer.data)
    
class OurValuesView(APIView):
    def get(self, request):
        company_overview = OurValues.objects.all()
        serializer = OurValuesSerializer(company_overview, many=True)
        return Response(serializer.data)
    