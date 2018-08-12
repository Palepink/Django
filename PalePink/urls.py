from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'home/$', views.home, name='home'),
    url(r'mall/$', views.Mall.as_view(), name='mall'),
]
app_name = 'PalePink'
