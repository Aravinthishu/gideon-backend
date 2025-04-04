from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
# Create your views here.



class EngineeringCapabilitiesView(APIView):
    def get(self, request, format=None):
        capabilities = EngineeringCapabilities.objects.all()
        serializer = EngineeringCapabilitiesSerializers(capabilities, many=True)
        return Response(serializer.data)
    
class ManufacturingInfrastructureView(APIView):
    def get(self, request, format=None):
        infrastructure = ManufacturingInfrastructure.objects.all()
        serializer = ManufacturingInfrastructureSerializers(infrastructure, many=True)
        return Response(serializer.data)
    
class MeasuringCapabilitiesView(APIView):
    def get(self, request, format=None):
        capabilities = MeasuringCapabilities.objects.all()
        serializer = MeasuringCapabilitiesSerializers(capabilities, many=True)
        return Response(serializer.data)