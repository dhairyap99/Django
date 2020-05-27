from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. 
# Deciding which template to run
# Connection with the models is done through view

def home(request):
    return render(request, 'home.html', {'name':'Dhairya'})

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    val3 = val1 + val2

    return render(request, 'result.html', {'result': val3})