from os import name
from django.urls import path
from . import views
app_name = 'administer'
urlpatterns = [
    path('panel', views.loginuser, name='login'),
    path('login', views.index, name='index'),
    path('register', views.regindex, name = 'regindex'),
    path('logout', views.logout, name='logout'),
    path('verified', views.registeruser, name="registeruser"),
    path('load', views.profile, name="load")

]
