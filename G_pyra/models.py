from django.db import models
import datetime as dt
import copy

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

  def save_category(self):
    '''
    function that helps in saving a category to the database
    '''
    self.save()  

  def delete_category(self):
    '''
    function that deletes a category from the database
    '''
    self.delete()

  
  # def update_category(cate_id,upd_categ):
  #   '''
  #   function that helps in writing an existing category
  #   '''
  #   cate=Category.objects.filter(id=cate_id)
  #   cate.name=upd_categ
  #   updated_cate=cate
  #   updated_cate.save()    
  #   return updated_cate

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

  def save_location(self):
    '''
    function that helps in saving a location
    '''
    self.save()  

  def delete_location(self):
    '''
    function that deletes a location from the database
    '''
    self.delete()

  # @classmethod
  # def update_location(cls,loc_id):
  #   '''
  #   function that helps in writing an existing location
  #   '''
  #   location=cls.objects.filter(id=loc_id)
  #   return location     

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

  def save_image(self):
    '''
    function that saves a new image to the database    
    '''
    self.save()

  def delete_image(self):
    '''
    function that deletes an image from the database
    '''
    self.delete()

  @classmethod
  def get_image_by_id(cls,image_id):
    '''
    function that helps in getting an  by id
    '''
    found=cls.objects.filter(id=image_id)
    return found
    
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

  class Meta:
    ordering=['image_name']      

  @classmethod
  def copy_image(cls,image_url):
    '''
    function that helps in copying the image url
    '''
    copied_element=copy.deepcopy(image_url)

    return copied_element

  def __str__(self):
      return self.image_name

  


  
  

