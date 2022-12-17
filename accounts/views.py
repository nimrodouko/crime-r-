from django.shortcuts import render
from django.views import generic
from .forms import *
from django.urls import reverse_lazy

class SignupView(generic.CreateView):
    template_name='signup.html'
    form_class = CustomCreation
    success_url =reverse_lazy('home')


# Create your views here.
