from django.test import TestCase
from .models import Image, Location, categories
# Create your tests here.


class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.James= Image(id = '1', image = 'example.jpg', name = 'James', description ='This is one of my favourite photos', location ='Nairobi', categories ='Portrait')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.James,Image)) 
    
     # Testing Save Method
    def test_save_method(self):
        self.James.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)       
        
class LocationTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Nairobi= Location(location='Nairobi')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))    
        
    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)    
        
    def test_delete_method(self):
        self.Nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)   
        
class categoriesTestClass(TestCase):       
      # Set up method
    def setUp(self):
        self.Portrait= categories(category='Portrait')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Portrait,categories))    
        
    def test_save_method(self):
        self.Portrait.save_category()
        categorie = categories.objects.all()
        self.assertTrue(len(categorie)>0)    
        
    def test_delete_method(self):
        self.Portrait.delete_category()
        categorie = categories.objects.all()
        self.assertTrue(len(categorie)==0)          