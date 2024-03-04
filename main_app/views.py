from django.shortcuts import render


class Destination:
  def __init__(self, name, country, description):
    self.name = name
    self.country = country
    self.description = description
    

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')