from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *


class CustomAdmin(UserAdmin):
    add_form = CustomCreation
    form = CustomChange
    model =CustomUser

admin.site.register(CustomUser, CustomAdmin)


# Register your models here.
