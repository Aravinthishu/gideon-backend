from django.db import models

# Create your models here.


class Award(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='awards/')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=250, blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    