from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.


class Topping_type(models.Model):
    toppingType = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.toppingType}"

class Topping(models.Model):
    topping = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.topping}"


class Standard_pizza(models.Model):
    topping = models.ForeignKey(Topping_type, on_delete=models.CASCADE)
    price_small = models.DecimalField(max_digits=6, decimal_places=2)
    price_large = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.id} / {self.topping} / {self.price_small} / {self.price_large}"

class Sicilian_pizza(models.Model):
    topping = models.ForeignKey(Topping_type, on_delete=models.CASCADE)
    price_small = models.DecimalField(max_digits=6, decimal_places=2)
    price_large = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return f"{self.id} / {self.topping} / {self.price_small} / {self.price_large}"


class Sub(models.Model):
    description = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.description} / {self.price_small} / {self.price_large}"

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
    price_small = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.description} / {self.price_small} / {self.price_large}"

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





      