from django.shortcuts import render
from .models import Destination
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def destination_index(request):
  destinations = Destination.objects.all()
  return render(request, 'destinations/index.html', {'destinations': destinations})

def destination_detail(request, destination_id):
  destination = Destination.objects.get(id=destination_id)
  return render(request, 'destinations/detail.html', { 'destination': destination }) 

class DestinationCreate(CreateView):
  model = Destination
  fields = '__all__'