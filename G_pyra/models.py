from django.db import models
import datetime as dt

class Category(models.Model):
  '''
  class that defines the categories for the images
  '''
  name=models.CharField(max_length=50)

  def __str__(self):
      return self.name

class Location(models.Model):
  '''
  class that defines Locations where the images were taken
  '''
  name=models.CharField(max_length=50)

  def __str__(self):
      return self.name

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

  def __str__(self):
      return self.image_name
  


  
  

