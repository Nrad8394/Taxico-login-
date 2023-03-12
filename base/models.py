from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    pickup_location =models.CharField(max_length=200)
    dropoff_location =models.CharField(max_length=200)
    date = models.DateField(null=True,blank=False)
    time = models.TimeField(null=True,blank=False)
    passengers = models.IntegerField(null=True,blank=False)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pickup_location
    
    class Meta:
        ordering = ['complete']