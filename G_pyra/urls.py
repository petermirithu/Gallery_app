from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home,name='home'),    
    url(r'^search/',views.search,name="searchRes"),
    url(r'^image/(\d+)',views.single_image,name="image"),
    url(r'^images/(Nairobi)',views.images_by_location,name="ImagesByLocation"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
