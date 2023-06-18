from django.db import models
from .managers import CustomManager
# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)

    objects=CustomManager()
    
    def __str__(self):
        return self.address
    
class Restaurant(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    serves_hot_dog=models.BooleanField(default=False)

    def __str__(self):
        return self.place.name
    
class Waiter(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.restaurant