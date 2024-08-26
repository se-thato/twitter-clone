from django.db import models
from django.contrib.auth.models import User

#create a User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #creating profile to be able to follow other profiles
    follows = models.ManyToManyField("self",
        related_name= "followed_by",
        symmetrical=False, #this means you can be able to follow somebody and they don't have to follow you back
        blank= True)
    
    def __str__(self):
        return self.user.username
    
    