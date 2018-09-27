from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extending user model using a one-to-one link
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gmail = models.CharField(max_length=255, blank=True)
	
class DataRequest(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created: # a new record was created
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()