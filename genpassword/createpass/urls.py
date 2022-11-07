from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about_site'),
    path('generate/', gen_pas, name='gen'),
    path('show_pas/', show_pas, name='show_pas'),
    path('cleardb', cleardb, name='cleardb')
]
