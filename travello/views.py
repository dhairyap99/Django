from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    #Times when we passed data from our model
    '''dest1 = Destination()    
    dest1.name = 'Bali'
    dest1.desc = 'The land of something for everyone'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Indonesia'
    dest2.desc = 'Wonderful Indonesia'
    dest2.img = 'destination_2.jpg'
    dest2.price = 300
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'San Francisco'
    dest3.desc = 'All within your reach'
    dest3.img = 'destination_3.jpg'
    dest3.price = 900
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Paris'
    dest4.desc = 'Rendez vous en France'
    dest4.img = 'destination_4.jpg'
    dest4.price = 800
    dest4.offer = False

    dest5 = Destination()
    dest5.name = 'Phi Phi Island'
    dest5.desc = 'The most enchanting island of Thailand'
    dest5.img = 'destination_5.jpg'
    dest5.price = 400
    dest5.offer = True

    dest6 = Destination()
    dest6.name = 'Mykonos'
    dest6.desc = 'Dance, drink, never sleep'
    dest6.img = 'destination_6.jpg'
    dest6.price = 600
    dest6.offer = False'''

    dests = Destination.objects.all()
  
    return render(request, 'index.html', {'dests': dests})