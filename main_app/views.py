from django.shortcuts import render, redirect
from .models import Destination
from .forms import VisitForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def destination_index(request):
  destinations = Destination.objects.filter(user=request.user)
  return render(request, 'destinations/index.html', {'destinations': destinations})

@login_required
def destination_detail(request, destination_id):
  destination = Destination.objects.get(id=destination_id)
  visit_form = VisitForm()
  return render(request, 'destinations/detail.html', { 'destination': destination, 'visit_form': visit_form }) 

@login_required
def add_visit(request, destination_id):
  form = VisitForm(request.POST)
  if form.is_valid():
    new_visit = form.save(commit=False)
    new_visit.destination_id = destination_id
    new_visit.save()
  return redirect('destination-detail', destination_id=destination_id)


class DestinationCreate(LoginRequiredMixin, CreateView):
  model = Destination
  fields = ['name', 'country', 'description', 'first_visit']

  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class DestinationUpdate(LoginRequiredMixin, UpdateView):
  model = Destination
  fields = '__all__'

class DestinationDelete(LoginRequiredMixin, DeleteView):
  model = Destination
  success_url = '/destinations/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('destination-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
