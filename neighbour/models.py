from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

LOCATION = [
  ('EAGLE COURT', 'Eagle'), 
  ('PEACOCK COURT', 'Peacock'), 
  ('SWAN COURT', 'Swan'), 
  ('SWALLOW COURT', 'Swallow'),
  ('SEAGULL COURT','Seagull'),
  ('FLAMINGO COURT','Flamingo'),
  ('ROBIN COURT','Robin'),
  ('KINGFISHER COURT','Kingfisher'),
]

TRADE = [
  ('PLUMBER', 'Plumber'),
  ('HAIR_SALON', 'Hair_Salon'),
  ('SHOP', 'Shop'),
  ('GYM', 'Gym'),
  ('GROCERY', 'Grocery'),
  ('CAPENTER', 'Capenter'),
  ('BUTCHERY','Butchery'),
  ('POLICE','Police'),
  ('HEALTH CENTRE','Health Center'),
  
  
  
]
class Neighbourhood(models.Model):
  name = models.CharField(max_length = 144)
  location = models.CharField(choices=LOCATION, default='Location', max_length=255)
  admin = models.ForeignKey(get_user_model(),  on_delete=models.CASCADE)
  occupants = models.PositiveIntegerField(default=0, blank=True)

  def __str__(self):
    return self.name

  def create(self):
    return self.save()

  def change(self):
    return self.save()

  def delete(self):
    return self.delete()
  
  def population(self):
    self.population +=1
    return self.save()

  def get_absolute_url(self):
    return reverse('neighbour_detail', args=[str(self.id)])


class Business(models.Model):
  name = models.CharField(max_length = 144)
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  email = models.EmailField(max_length=255, blank=True)
  business_type = models.CharField(choices=TRADE, default='Business', max_length=255)

  def __str__(self):
    return self.name

  def create_business(self):
    return self.save()

  def change_business(self):
    return self.save()

  def delete_business(self):
    return self.delete()
  
  def get_absolute_url(self):
    return reverse('business_detail', args=[str(self.id)])

class Conversation(models.Model):
  topic = models.CharField(max_length = 100)
  member = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
  details = models.TextField()

  def __str__(self): 
    return self.topic

  def get_absolute_url(self):
    return reverse('conversation', args=[str(self.id)])


