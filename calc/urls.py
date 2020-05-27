from django.urls import path
from . import views

#Sending a navigation to decide which view to go-to

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add')

    ]