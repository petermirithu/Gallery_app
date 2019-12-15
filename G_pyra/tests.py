from django.test import TestCase
from .models import Category,Location,Image
import pyperclip

class CategoryTestCase(TestCase):
  '''
  class that helps in testing all functions under the category model
  '''
  def setUp(self):
    '''
    Testcase to create new category  object for test purposes
    '''
    self.category1=Category(name='Landscape')
    self.category2=Category(name='Portrait')
  def test_instance(self):
    '''
    Testcase for testing instances of category objects
    '''
    self.assertTrue(isinstance(self.category1,Category))
    self.assertTrue(isinstance(self.category2,Category))

  def test_save(self):
    '''
    Testcase to test on saving a new category to the database
    '''
    self.category1.save_category()
    self.category2.save_category()
    categories=Category.objects.all()
    self.assertEquals(len(categories),2)

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    ''' 
    Category.objects.all().delete()
    
  def test_delete(self):
    '''
    Testcase to test on deleting a category from the database
    '''
    self.category1.save_category()
    self.category2.save_category()    
    self.category1.delete_category()
    categories=Category.objects.all()
    self.assertTrue(len(categories)<2)

  # def test_update(self):
  #   '''
  #   Testcase to test on updating or rewriting a category
  #   '''
  #   self.category1.save_category()
  #   self.category2.save_category()

  #   self.category.update_category(cate_id=self.category2.id,upd_categ='wildlife')

  #   self.assertTrue(self.upd.name=='wildlife')

  def test_get_category(self):
    '''
    Testcase to test on getting category from a search term
    '''
    self.category1.save_category()
    self.category2.save_category()   

    found_cate=Category.search_category('Landscape')

    self.assertEquals(len(found_cate),1)


class LocationTestCase(TestCase):
  '''
  class that tests all functions under the Location model
  '''
  def setUp(self):
    '''
    Testcase to create new location  object for test purposes
    '''
    self.location1=Location(name='Nairobi')
    self.location2=Location(name='Arusha')
  def test_instance(self):
    '''
    Testcase for testing instances of Location objects
    '''
    self.assertTrue(isinstance(self.location1,Location))
    self.assertTrue(isinstance(self.location2,Location))

  def test_save(self):
    '''
    Testcase to test on saving a location to the database
    '''
    self.location1.save_location()
    self.location2.save_location()
    locations=Location.objects.all()
    self.assertEquals(len(locations),2)

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    '''     
    Location.objects.all().delete()
    
  def test_delete(self):
    '''
    Testcase to test on deleting a location from the database
    '''
    self.location1.save_location()
    self.location2.save_location()
    self.location1.delete_location()
    locs=Location.objects.all()
    self.assertTrue(len(locs)<2)

  # def test_update(self):
  #   '''
  #   Testcase to test on updating or rewriting a category
  #   '''
  #   self.category1.save_category()
  #   self.category2.save_category()

  #   self.category1.update_category(self.category2.id)
  #   self.assertTrue(category1.name='Arusha')

  def test_get_location(self):
    '''
    Testcase to test on getting a location from a search term
    '''
    self.location1.save_location()
    self.location2.save_location()  

    found_loc=Location.get_location('Nairobi')

    self.assertEquals(len(found_loc),1)


class ImageTestCase(TestCase):
  '''
  Testcase  class to test on all function associated with the image class
  '''
  def setUp(self):
    '''
    Testcase to create test  objects for location,category & Image.
    '''
    # Locations
    self.location1=Location(name='Nairobi')
    self.location2=Location(name='Arusha')
    self.location1.save_location()
    self.location2.save_location()

  # Categories
    self.category1=Category(name='Landscape')
    self.category2=Category(name='Portrait')
    self.category1.save_category()
    self.category2.save_category()

  # Images
    self.image1=Image(image_name="Waterfall",image_url="images/waterfall.jpg",description='It a sunny day at Thomson Park',posted_on="2019-12-08",category=self.category1,location=self.location1)
    self.image2=Image(image_name="Pyra's pic",image_url="images/pyraPortraitjpg",description='Its portrait image of Pyra',posted_on="2019-10-04",category=self.category2,location=self.location2)
    self.image1.save_image()
    self.image2.save_image()


  def test_instance(self):
    '''
    Testcase for testing instances of an Image object
    '''
    self.assertTrue(isinstance(self.image1,Image))
    self.assertTrue(isinstance(self.image2,Image))

  def tearDown(self):   
    '''
    Testcase that delete all objects after every test has run
    ''' 
    Category.objects.all().delete()
    Location.objects.all().delete()
    Image.objects.all().delete()

  def test_save(self):
    '''
    Testcase to test on saving an image to the database
    '''
    self.image1.save_image()
    self.image2.save_image()
    
    savedimages=Image.objects.all()
    self.assertEquals(len(savedimages),2)

  def test_delete(self):
    '''
    Testcase to test on deleting an image from the database
    '''
    self.image1.save_image()
    self.image2.save_image()

    self.image1.delete_image()    
    savedimages=Image.objects.all()
    self.assertEquals(len(savedimages),1)
  
  def test_get_image_by_id(self):
    '''
    Testcase to test on getting a single image by id
    '''    
    self.image1.save_image()
    self.image2.save_image()

    try:
      found=Image.get_image_by_id(self.image1.id)      
      
    except ValueError:

      raise AttributeError
      
    self.assertEquals(len(found),1)

  def test_search(self):
    '''
    Testcase to test on searching for an image by category
    '''
    self.image1.save_image()
    self.image2.save_image()

    search_term='Landscape'
    found_cate=Category.search_category(search_term)
    results=Image.search_image(found_cate)

    self.assertEquals(len(results),1)

  def test_get_images_by_location(self):
    '''
    Testcase to test on getting images by location
    '''
    self.image1.save_image()
    self.image2.save_image()

    search_term='Arusha'
    found_image_locs=Location.get_location(search_term)
    results=Image.get_images_by_location(found_image_locs)

    self.assertEquals(len(results),1)

  def test_copy_image(self):
    '''
    Testcase to test on copying an image url
    '''
    self.image1.save_image()
    self.image2.save_image()

    Image.copy_image(self.image2.image_url.url)

    self.assertEquals(self.image2.image_url.url,pyperclip.paste())
    

