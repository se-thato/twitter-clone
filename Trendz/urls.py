from django.urls import path
from . import views

urlpatterns = [
    #creating a home page
   path('', views.home, name='home')
]
