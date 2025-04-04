from rest_framework import serializers
from .models import *

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerForm
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'
        
class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__'