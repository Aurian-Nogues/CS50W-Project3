from django.db import models

# Create your models here.

class Pasta(models.Model):
    description = models.CharField(max_length=64)
    price = models.FloatField(max_length=8)
    
    def __str__(self):
        return f"{self.id} - {self.description} : {self.price}"


class Flavour(models.Model):
    flavour = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.id} - {self.flavour}"


class Size(models.Model):
    size = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.id} - {self.size}"


class ToppingType(models.Model):
    toppingType = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.id} - {self.toppingType}"

""" class Pizza(models.Model):
    flavour = models.ForeignKey(Flavours, on_delete=models.CASCADE, related_name='pizza_flavour')
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, related_name='pizza_size')
    topping = models.ForeignKey(ToppingTypes, on_delete=models.CASCADE, related_name='pizza_toppingType')
    price = models.FloatField(max_length=8)

    def __str__(self):
        return f"{self.id} - {self.flavour} / {self.size} / {self.topping} / {self.price}"
 """



      