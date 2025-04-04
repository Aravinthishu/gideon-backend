from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class MilestoneView(APIView):
    def get(self, request):
        milestones = Milestone.objects.all()
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)