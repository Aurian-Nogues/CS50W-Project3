from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Pasta, Standard_pizza, Sicilian_pizza, Salad, Platter, Sub, Topping, Orders_list, Orders_tracking
from.models import UserCreationForm
from django.urls import reverse

# Create your views here.

#If thre are no orders, set first order_number to 0
try:
    last_order = Orders_tracking.objects.order_by('-id')[0]
except IndexError:
    print("order list is empty, first order number set to 0")
    global_order_number = 0



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
    global global_order_number

    if request.is_ajax() and request.POST:
        data = {'message': "Pizza added"}

        user=request.user

        item = request.POST.get('item')
        toppings = request.POST.get('toppings')
        price = request.POST.get('price')

        print("                      I am Here                 ")
        print("")
        print("///////////////////////////////")
        print(user)
        #check if user has open order and get order number. If not create one
        try:
            open_order = Orders_tracking.objects.all().get(user=user, status="open")
            print("///////////////////////////////")

            print(open_order)
        except ObjectDoesNotExist:
            print("no open order, creating a new order number")
            #create an open order and increase global order number by 1
            global_order_number = global_order_number + 1
            order_number = global_order_number
            entry = Orders_tracking(user=user, order_number=order_number, status="open")
            entry.save()
            print("///////////////////////////////")
            print("///////////////////////////////")
            print("No open orders, created one")



        #get order number from open order
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
        order_number = open_order.order_number
        print("got order number from open order")

        entry=Orders_list(order_number=order_number, item=item, toppings_extras=toppings, price=price)
        entry.save()

        return HttpResponse()

    else:
        raise Http404
