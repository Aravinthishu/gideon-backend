from django.db import models

# Create your models here.


class Expertise(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class CeosDesk(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    designation = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='ceos_desk/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name