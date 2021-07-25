from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('mba', views.mba, name='mba'),
    path('eng', views.eng, name='eng'),
    path('arts', views.arts, name='arts'),
    path('about', views.about, name='about'),
    path('compare', views.compare, name='compare'),
    path('compareRes', views.compareRes, name='compareRes'),
    path('predictions', views.prediction, name='predictions'),
    path('mbaRating', views.mbaRating, name='mbaRating'),
    path('predRes', views.predRes, name='predRes'),
]