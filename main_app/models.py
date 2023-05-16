from django.db import models
from django.urls import reverse
import json
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Funko(models.Model):
    name = models.CharField(max_length=200)
    association = models.CharField(max_length=200, blank=True)
    series = models.CharField(max_length=200)
    number = models.IntegerField()
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('funko_detail', kwargs={'pk': self.id})
    
class Profile(models.Model):
    collection = models.ManyToManyField(Funko, related_name="collection_profiles", symmetrical=False, blank=True)
    wishlist = models.ManyToManyField(Funko, related_name="wishlist_profiles", symmetrical=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.user)

#Create profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)
