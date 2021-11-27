from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=60)
    
    def __str__(self):
        return self.location 
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    class Meta:
        ordering = ['location']
       
       
class categories(models.Model):
    category = models.CharField(max_length=60)
     
    def __str__(self):
        return self.category    
    
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    class Meta:
        ordering = ['category']       
       