from rest_framework import serializers
from .models import *


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'
        
class CeosDeskSeiralizers(serializers.ModelSerializer):
    class Meta:
        model = CeosDesk
        fields = '__all__'