from rest_framework import serializers
from .models import *


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = '__all__'
        
class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'