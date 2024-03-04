from django.shortcuts import render


class Destination:
  def __init__(self, name, country, description):
    self.name = name
    self.country = country
    self.description = description
    

destinations = [
  Destination('Universal Studios', 'United States', 'Super fun place to go! But do not go during the summer because you could potentially melt.'),
  Destination('Disney', 'United States', 'Apparently it is frowned upon to jump out of the boats on water rides here. Ridiculous.'),
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def destination_index(request):
  return render(request, 'destinations/index.html', {'destinations': destinations})