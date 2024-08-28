from django.urls import path
from . import views

urlpatterns = [
    #creating a home page
   path('', views.home, name='home'),
   path('profile_list/', views.profile_list, name='profile_list'),
]
