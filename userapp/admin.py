from django.contrib import admin

# Register your models here.
from .models import UserDetails
# registering the user
admin.site.register(UserDetails)
