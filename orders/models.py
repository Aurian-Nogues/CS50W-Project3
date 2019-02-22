from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Flavour(models.Model):
    flavour = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.flavour}"


class Size(models.Model):
    size = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.size}"


class Topping_type(models.Model):
    toppingType = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.toppingType}"

class Topping(models.Model):
    topping = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.topping}"


class Pizza(models.Model):
    flavour = models.ForeignKey(Flavour, on_delete=models.CASCADE, related_name='pizza_flavour')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='pizza_size')
    topping = models.ForeignKey(Topping_type, on_delete=models.CASCADE, related_name='pizza_toppingType')
    price = models.FloatField(max_length=8)

    def __str__(self):
        return f"{self.id} - {self.flavour} / {self.size} / {self.topping} / {self.price}"


class Pasta(models.Model):
    description = models.CharField(max_length=64)
    price = models.FloatField(max_length=8)
    
    def __str__(self):
        return f"{self.description} / {self.price}"


class Salad(models.Model):
    description = models.CharField(max_length=64)
    price = models.FloatField(max_length=8)

    def __str__(self):
        return f"{self.description} / {self.price}"


class Platter(models.Model):
    description = models.CharField(max_length=64)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='platter_size')
    price = models.FloatField(max_length=8)

    def __str__(self):
        return f"{self.description}  / {self.size} / {self.price}"

#create custom registration form extending Django UserCreationForm
class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required = True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user=super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user







      