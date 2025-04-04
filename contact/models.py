from django.db import models

# Create your models here.
class CareerForm(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    area_of_expertise = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class JobPosition(models.Model):
    position = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.position