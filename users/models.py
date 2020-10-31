from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from . import roles


class CustomUser(AbstractUser):
  date_joined = models.DateTimeField(default = timezone.now)
  user_type = models.PositiveSmallIntegerField(choices = roles.USER_TYPE_CHOICES, default = 1)

  

class UserProfile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name = 'profile')
  first_name = models.CharField(max_length = 255, blank=True)
  middle_name = models.CharField(max_length = 255, blank=True)
  last_name = models.CharField(max_length = 255, blank=True)
  email = models.EmailField(max_length =255, blank=True, null = True)
  gok_id = models.PositiveIntegerField(default=0, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  changed_at = models.DateTimeField(auto_now=True)
  #neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='user_profile')

  def __str__(self): 
    return 'User: {}'.format(self.user)
  
  # def get_absolute_url(self):
  #   return reverse('signup', args=[str(self.id)])

  
 
