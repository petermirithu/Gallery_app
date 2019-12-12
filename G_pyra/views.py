from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

def home(request):
  '''
  view function that renders the home page on application's start up
  '''  
  return render(request,'home.html')


