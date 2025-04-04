from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class WhoWeAreSection(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='who_we_are/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class OurMissionVision(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    icon = models.ImageField(upload_to='our_mission_vision/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    
class OurValues(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='our_values/', null=True, blank=True)

    def __str__(self):
        return self.title