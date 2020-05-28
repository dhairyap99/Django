from django.urls import path
from . import views

#Sending a navigation to decide which view to go-to

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')   

    ]