from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister group from your admin 
admin.site.unregister(Group)


#combine Profile information together with the User information
class ProfileInline(admin.StackedInline):
    model = Profile

#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    #displaying username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]


#unregister initial user
admin.site.unregister(User)

#Reregister  user and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)


