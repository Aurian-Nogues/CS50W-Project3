from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Pasta, Standard_pizza, Sicilian_pizza, Salad, Platter, Sub, Topping, Orders_list, Orders_tracking
from.models import UserCreationForm
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    return HttpResponseRedirect(reverse("home"))

def home(request):
    context = {

    }
    return render(request, "orders/home.html", context)


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def createAccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return HttpResponseRedirect(reverse("index"))
    else:      
        form = UserCreationForm()

    return render(request, "orders/createAccount.html", {'form': form})

def pizzas(request):
    Standard_pizza_list = Standard_pizza.objects.all()  
    Sicilian_pizza_list = Sicilian_pizza.objects.all()
    context = {
        "user": request.user,
        "Standard_pizzas": Standard_pizza_list,
        "Sicilian_pizzas": Sicilian_pizza_list,
    }
    return render(request, "orders/pizzas.html", context)


def subs(request):
    Subs = Sub.objects.all()
    context = {
        "user": request.user,
        "Subs": Subs,
    }    
    return render(request, "orders/subs.html", context)

def pastas(request):
    Pastas = Pasta.objects.all()
    context = {
        "user": request.user,
        "Pastas": Pastas,
    }    
    return render(request, "orders/pastas.html", context)

def salads(request):
    Salads = Salad.objects.all()
    context = {
        "user": request.user,
        "Salads": Salads,
    }    
    return render(request, "orders/salads.html", context)

def platters(request):
    Platters = Platter.objects.all()
    context = {
        "user": request.user,
        "Platters": Platters,
    }    
    return render(request, "orders/platters.html", context)

def pizza_toppings(request,description, topping, price):
    Toppings = Topping.objects.all()
    

    #test topping allowance
    if topping == "Cheese":
        counter=0
    if topping == "1 topping":
        counter=1
    if topping == "2 toppings":
        counter=2
    if topping == "3 toppings":
        counter=3
    if topping == "Special":
        counter=5

    context = {
    "user": request.user,
    "counter": counter,
    "description": description,
    "topping": topping,
    "price": price,
    "Toppings": Toppings,
    }    
    return render(request, "orders/toppings.html", context)

#Ajax request handler to add pizza to basket
def add_pizza(request):
    if request.is_ajax() and request.POST:
        data = {'message': "%s added" % request.POST.get('item')}

        user=request.user

        item = request.POST.get('item')
        toppings = request.POST.get('toppings')
        price = request.POST.get('price')

        #check if user has open order and get order number. If not create one
        #"Checkout":Order2.objects.filter(user=request.user,number=order_number),
        order_number = Orders_tracking.objects.all().filter(user=user, status="open")
        if not order_number:
            print("no open order")
        print(order_number)

        print(user)
        print(item)
        print(toppings)
        print(price)


        return HttpResponse(json.dumps(data), content_type='application/json')

    else:
        raise Http404


