from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'), 
  path('destinations/', views.destination_index, name='destination-index'),
  path('destinations/<int:destination_id>/', views.destination_detail, name='destination-detail'),
  path('destinations/create/', views.DestinationCreate.as_view(), name='destination-create'),
  path('destinations/<int:pk>/update/', views.DestinationUpdate.as_view(), name='destination-update'),
  path('destinations/<int:pk>/delete/', views.DestinationDelete.as_view(), name='destination-delete'),
]