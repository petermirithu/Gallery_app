from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist

def home(request):
  '''
  view function that renders the home page on application's start up
  '''  
  return render(request,'home.html')

def search(request):
  if 'pics' in request.GET and request.GET["pics"]:
    search_term=request.GET.get('pics')
    category_res=Category.search_category(search_term)    
    results=Image.search_image(category_res)
    if results:
      message=f"{search_term}"  
      title='Results'

      return render(request,'search.html',{"message":message,"images":results,"title":title})

    else:
      message="You haven't search for a category"  
      title='Results'
      return render(request, 'search.html',{"message":message,"title":title})

def images_by_location(request, location_name):
  '''
  view function that renders images based on location picked
  '''  
  try:
    found_location=Location.get_location(location_name)
    images=Image.get_images_by_location(found_location)    
    title=location_name
    
  except ObjectDoesNotExist:
    raise Http404()

  return render(request, 'images.html',{"images":images,"title":title})

def images_by_category(request, category_name):
  '''
  view function that renders all images with same category
  '''
  try:
    found_category=Category.search_category(category_name)
    images=Image.search_image(found_category)    
    title=category_name
    
  except ObjectDoesNotExist:
    raise Http404()

  return render(request, 'Bycategory.html',{"images":images,"title":title})


