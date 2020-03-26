from django.shortcuts import render
from .models import Destination
from .models import maza
# Create your views here.
def index(request):

    dests = Destination.objects.all()
    
    cap = maza()
    cap.img = "dynimg1.jpg"
    return render(request, "index.html", {'dests': dests,"p":cap.img})
