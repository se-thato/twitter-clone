from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#create a User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #creating profile to be able to follow other profiles
    follows = models.ManyToManyField("self",
        related_name= "followed_by",
        symmetrical=False, #this means you can be able to follow somebody and they don't have to follow you back
        blank= True)
    date_modified= models.DateTimeField(User, auto_now=True) #to show when was the last time they modified their data



    def __str__(self):
        return self.user.username
    
    
#create profile when new user Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        #Making the user follow themselves auto.. after creating their profile
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)

#