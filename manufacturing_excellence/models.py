from django.db import models

# Create your models here.


class EngineeringCapabilities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='engineering_capabilities/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ManufacturingInfrastructure(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Manufacturing_infrastructure/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class MeasuringCapabilities(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='measuring_capabilities/', null=True, blank=True)
    icon = models.ImageField(upload_to='measuring_capabilities/', null=True, blank=True)
    
    def __str__(self):
        return self.name