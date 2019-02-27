from django.http import HttpResponse, Http404, HttpResponseRedirect
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Pasta, Standard_pizza, Sicilian_pizza, Salad, Platter, Sub, Topping, Orders_list, Orders_tracking
from.models import UserCreationForm
from django.urls import reverse

#//////////////////////Global variables/////////////////////////////

#If thre are no orders, set first order_number to 0
#if there are database entries set variable to last order in DB
try:
    global_order_number_entry = Orders_tracking.objects.order_by('-id')[0]
    global_order_number = global_order_number_entry.order_number
except IndexError:
    print("order list is empty, create initial order number")
    global_order_number = 0

#///////////////////////////////////////////////////////////////////

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

def subs_extras(request, description, size, price):

    context = {
        "user": request.user,
        "description": description,
        "size": size,
        "price": price
    }
    return render(request, "orders/subs_extras.html", context)


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
    #import global variable to get order number
    global global_order_number

    if request.is_ajax() and request.POST:
        user=request.user
        item = request.POST.get('item')
        toppings = request.POST.get('toppings')
        price = request.POST.get('price')

        #check if user has open order and get order number. If not create one
        try:
            open_order = Orders_tracking.objects.all().get(user=user, status="open")
        except ObjectDoesNotExist:
            print("no open order for user, creating a new order number")
            #create an open order and increase global order number by 1
            global_order_number = global_order_number + 1
            order_number = global_order_number
            entry = Orders_tracking(user=user, order_number=order_number, status="open")
            entry.save()

        #get order number from open order
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
        order_number = open_order.order_number
        print("got order number from open order")

        #add new order to order_list
        entry=Orders_list(order_number=order_number, item=item, toppings_extras=toppings, price=price)
        entry.save()

        return HttpResponse()

    else:
        raise Http404

#Ajax request handler to add sub to basket
def add_sub(request):
    #import global variable to get order number
    global global_order_number

    if request.is_ajax() and request.POST:
        user=request.user
        item = request.POST.get('item')
        extras = request.POST.get('extras')
        price = request.POST.get('price')

        #check if user has open order and get order number. If not create one
        try:
            open_order = Orders_tracking.objects.all().get(user=user, status="open")
        except ObjectDoesNotExist:
            print("no open order for user, creating a new order number")
            #create an open order and increase global order number by 1
            global_order_number = global_order_number + 1
            order_number = global_order_number
            entry = Orders_tracking(user=user, order_number=order_number, status="open")
            entry.save()

        #get order number from open order
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
        order_number = open_order.order_number
        print("got order number from open order")

        #add new order to order_list
        entry=Orders_list(order_number=order_number, item=item, toppings_extras=extras, price=price)
        entry.save()

        return HttpResponse()

    else:
        raise Http404

def add_pasta_salad(request, description, price):
    #import global variable to get order number
    global global_order_number

    user=request.user
    item = description

    #check if user has open order and get order number. If not create one
    try:
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
    except ObjectDoesNotExist:
        print("no open order for user, creating a new order number")
        #create an open order and increase global order number by 1
        global_order_number +=1
        order_number = global_order_number
        entry = Orders_tracking(user=user, order_number=order_number, status="open")
        entry.save()

    #get order number from open order
    open_order = Orders_tracking.objects.all().get(user=user, status="open")
    order_number = open_order.order_number
    print("got order number from open order")

    #add new order to order_list
    entry=Orders_list(order_number=order_number, item=item, price=price)
    entry.save()

    context = {
    }
    return HttpResponseRedirect(reverse("home"))

def add_platter(request, description,size, price):
    #import global variable to get order number
    global global_order_number

    user=request.user
    item = size + " " + description

    #check if user has open order and get order number. If not create one
    try:
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
    except ObjectDoesNotExist:
        print("no open  for user, creating a new order number")
        #create an open order and increase global order number by 1
        global_order_number +=1
        order_number = global_order_number
        entry = Orders_tracking(user=user, order_number=order_number, status="open")
        entry.save()

    #get order number from open order
    open_order = Orders_tracking.objects.all().get(user=user, status="open")
    order_number = open_order.order_number
    print("got order number from open order")

    #add new order to order_list
    entry=Orders_list(order_number=order_number, item=item, price=price)
    entry.save()

    context = {
    }
    return HttpResponseRedirect(reverse("home"))


def cart(request):
    user=request.user

    #test if user has an open order
    try:
        open_order = Orders_tracking.objects.all().get(user=user, status="open")
    except ObjectDoesNotExist:
        return render(request, "orders/error.html", {"message": "No open order."})

    #get open order number
    open_order = Orders_tracking.objects.all().get(user=user, status="open")
    order_number = open_order.order_number

    #test if user has items in open order
    try:
        orders = Orders_list.objects.all().filter(order_number=order_number)
    except ObjectDoesNotExist:
        return render(request, "orders/error.html", {"message": "No items in order."})
    

    count = orders.count()
    if count == 0:
        return render(request, "orders/error.html", {"message": "No items in order."})
    
    #if user has an open order and has items in it:

    #calculate total order amount
    total=0
    for instance in orders:
        total += instance.price
    context = {
        "Orders": orders,
        "order_number": order_number,
        "total_amount": total,
    }
    return render(request, "orders/cart.html", context)

#Ajax request handler to remove items from basket
def delete_item(request):
    if request.is_ajax() and request.POST:
        item = request.POST.get('item')
        price = request.POST.get('price')
        extras = request.POST.get('extras')
        order_number = request.POST.get('order_number')

        if extras == "None":
            order = Orders_list.objects.all().get(item=item, order_number=order_number)
        else:
            order = Orders_list.objects.all().get(item=item, order_number=order_number, toppings_extras=extras)
        order.delete()

        return HttpResponse()

    else:
        raise Http404

#Ajax request handler to remove items from basket
def confirm_order(request):
    if request.is_ajax() and request.POST:
        
        order_number = request.POST.get('order_number')
        try:
            order = Orders_tracking.objects.all().get(order_number=order_number)
        except ObjectDoesNotExist:
            return render(request, "orders/error.html", {"message": "Order does not exist."})

        print(order)
        order.status = "Confirmed"
        order.save()
        print(order)
        return HttpResponse()
    
    else:
        raise Http404