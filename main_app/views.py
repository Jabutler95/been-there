from django.shortcuts import render
from .models import Destination
from .forms import VisitForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
  visit_form = VisitForm()
  return render(request, 'destinations/detail.html', { 'destination': destination, 'visit_form': visit_form }) 

class DestinationCreate(CreateView):
  model = Destination
  fields = '__all__'

class DestinationUpdate(UpdateView):
  model = Destination
  fields = '__all__'

class DestinationDelete(DeleteView):
  model = Destination
  success_url = '/destinations/'