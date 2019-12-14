from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url('^$',views.home,name='home'),    
    url(r'^search/',views.search,name="searchRes"),    
    path('images/<str:location_name>',views.images_by_location,name="ImagesByLocation"),
    path('category/<str:category_name>',views.images_by_category,name="ImagesByCategory"),
    path('copy/images/<str:image_url>',views.copy_image_url,name="copyUrl"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
