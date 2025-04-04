from rest_framework import serializers
from .models import *


class WhoWeAreSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoWeAreSection
        fields = '__all__'
        
class OurMissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMissionVision
        fields = '__all__'
        
class OurValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurValues
        fields = '__all__'