from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile

@receiver(post_save, sender=CustomUser)
def create_change_userprofile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)
  instance.profile.save()
