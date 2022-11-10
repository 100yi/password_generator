from django.urls import path
from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about_site'),
    path('generate/', gen_pas, name='gen'),
    path('show_pas/', show_pas, name='show_pas'),
    path('cleardb/', cleardb, name='cleardb'),

    path('ru/index/', index_ru, name='index_ru'),
    path('ru/about/', about_ru, name='about_site_ru'),
    path('ru/generate/', gen_pas_ru, name='gen_ru'),
    path('ru/show_pas/', show_pas_ru, name='show_pas_ru'),
]
