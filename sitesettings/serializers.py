from rest_framework import serializers
from .models import *

class Sitesettings_serializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        
class SocialLinks_serializers(serializers.ModelSerializer):
    class Meta:
        model = Social_links
        fields = '__all__'