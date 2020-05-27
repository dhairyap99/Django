from django.urls import path
from . import views

#Sending a navigation to decide which view to go-to

urlpatterns = [
    path('', views.index, name='index')
    
    ]