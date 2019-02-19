from django.db import models

# Create your models here.

class Pasta(models.Model):
    description = models.CharField(max_length=64)
    price = models.FloatField(max_length=8)
    
    def __str__(self):
        return f"{self.id} - {self.description} : {self.price}"

class Categories(models.Model):
    flavour = models.CharField(max_length=16)
    size = models.CharField(max_length=16)
    toppingType = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} - {self.flavour} / {self.size} / {self.toppingType}"



      