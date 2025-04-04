from rest_framework import serializers
from .models import *


class CategorySerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ClientLogoSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = ClientLogo
        fields = '__all__'