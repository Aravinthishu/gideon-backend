from django.urls import path, include
from . import views

urlpatterns = [
    path('Engineering-capabilities', views.EngineeringCapabilitiesView.as_view(), name='EngineeringCapabilitiesView'),
    path('manufacturing-infrastructure', views.ManufacturingInfrastructureView.as_view(), name='ManufacturingInfrastructureView'),
    path('measuring-capabilities', views.MeasuringCapabilitiesView.as_view(), name='MeasuringCapabilitiesView'),
]
