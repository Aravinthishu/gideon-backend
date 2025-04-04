from rest_framework import serializers
from .models import Milestone, MilestoneImage

class MilestoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneImage
        fields = ['image']

class MilestoneSerializer(serializers.ModelSerializer):
    images = MilestoneImageSerializer(many=True, read_only=True)

    class Meta:
        model = Milestone
        fields = ['id', 'title', 'description', 'icon', 'year', 'images']
