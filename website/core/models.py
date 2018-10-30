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
	
class Image(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=1000)
	image = models.FileField(upload_to='diagrams')
	
	def image_tag(self):
		return mark_safe('<img src="\website\core\static\admin\images\ER-Diagram.png" />')
	
	image_tag.short_description = 'ER-Diagram'
	
	def __str__(self):
		return self.title
		
class Category(models.Model):
	Image = models.ForeignKey(Image, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name	
	
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created: # a new record was created
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.userprofile.save()
	