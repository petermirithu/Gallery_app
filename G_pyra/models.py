from django.db import models
import datetime as dt

class Category(models.Model):
  '''
  class that defines the categories for the images
  '''
  name=models.CharField(max_length=50)

  def __str__(self):
      return self.name

  @classmethod
  def search_category(cls,category):
    '''
    function tha searches the inputed search-term if it matches any category and returns the category
    '''
    category=cls.objects.filter(name=category)
    return category


class Location(models.Model):
  '''
  class that defines Locations where the images were taken
  '''
  name=models.CharField(max_length=50)

  def __str__(self):
      return self.name

  @classmethod
  def get_location(cls,location):
    '''
    function that gets location with is equal to the arguement passed for location
    '''
    location=cls.objects.filter(name=location)
    return location


class Image(models.Model):
  '''
  class that defines how an image is stored in the database
  '''
  image_name=models.CharField(max_length=30)
  image_url=models.ImageField(upload_to='images/',blank=True)
  description=models.CharField(max_length=500)
  posted_on=models.DateField(auto_now_add=True)  
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  location=models.ForeignKey(Location,on_delete=models.CASCADE)  
  @classmethod
  def search_image(cls,search_term):
    '''
    function that helps in searching for an image by Category
    '''
    images=cls.objects.filter(category__in=search_term)
    return images

  @classmethod
  def get_images_by_location(cls,location_name):
    '''
    function that gets all images with the same location
    '''
    images=cls.objects.filter(location__in=location_name) 
    return images
    
  def __str__(self):
      return self.image_name
  


  
  

