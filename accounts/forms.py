from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class CustomCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =UserCreationForm.Meta.fields +('ID_Number',)

class CustomChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
