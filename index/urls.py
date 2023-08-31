
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('product/', views.product, name='product'),
    

]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
