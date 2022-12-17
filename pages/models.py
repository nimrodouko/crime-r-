from django.db import models
from django.urls import reverse
from accounts.models import CustomUser






class Posts(models.Model):

    

    description = models.TextField(max_length=600)
    image = models.FileField(upload_to='covers/' ,blank=True, null=True,)
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])

    
    
   
class Wanted(models.Model):
    Name = models.CharField(max_length=15)
    origin = models.CharField(max_length=10)
    image = models.FileField(upload_to='covers/')
    reward = models.IntegerField(null=True)


    def get_absolute_url(self):
        return reverse('home',args=[str(self.id)])

    def __str__(self):
        return self.Name

