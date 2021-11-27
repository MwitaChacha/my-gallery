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
       
       
class Image(models.Model):
    image = CloudinaryField('image')
    name =  models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    categories = models.ManyToManyField(categories) 
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()    
    
    def get_image_by_id(id):
        image = Image.objects.get(id)
        return image
        
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images    
    
    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(categories__category=search_term)
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = cls.objects.filter(location__location=location).all()
        return image_location       