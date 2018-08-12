from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Image/$', views.image, name='Image'),
]
app_name = 'photo'
