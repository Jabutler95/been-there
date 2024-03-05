from django.db import models
from django.urls import reverse
from datetime import date

# RATING = (
#   1, 2, 3, 4, 5
# )

# Create your models here.
class Destination(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  date = models.DateField(default=date.today)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('destination-detail', kwargs={'destination_id': self.id})
  
# class Review(models.Model):
#   rating = models.CharField(
#     choices=RATING,
#     default=RATING[4]
#   )
#   notes = models.CharField(max_length=500)

#   def __str__(self):
#     return 