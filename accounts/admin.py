from django.contrib import admin
from .forms import *
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomAdmin(UserAdmin):
    add_form = CustomCreation
    form = CustomChange
    model =CustomUser

admin.site.register(CustomUser, CustomAdmin)


# Register your models here.
