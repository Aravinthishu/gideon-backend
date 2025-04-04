from rest_framework import serializers
from .models import *


class EngineeringCapabilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EngineeringCapabilities
        fields = '__all__'
        
class ManufacturingInfrastructureSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManufacturingInfrastructure
        fields = '__all__'
        
class MeasuringCapabilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeasuringCapabilities
        fields = '__all__'