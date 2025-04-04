import os
from django.db import models
from django.dispatch import receiver
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete image file if exists
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)

class ClientLogo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='clientlogos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # Delete image file if exists
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(self.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)
