from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class MainProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='mainproducts/', null=True, blank=True)
    image2 = models.ImageField(upload_to='mainproducts/', null=True, blank=True)
    background_image = models.ImageField(upload_to='bg-image', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Slug field
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    MainProduct = models.ForeignKey(MainProduct, on_delete=models.CASCADE)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Slug field
    
    def __str__(self):
        return self.name
    