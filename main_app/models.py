from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date




# Create your models here.
class Destination(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  first_visit = models.DateField(default=date.today)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('destination-detail', kwargs={'destination_id': self.id})
  
class Visit(models.Model):
  date = models.DateField('Visit Date')


  destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_visit_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']