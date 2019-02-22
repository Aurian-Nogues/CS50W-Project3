from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Pasta, Pizza, Salad, Platter
from.models import UserCreationForm
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    pizzas_list = Pizza.objects.all()
    pizza_table = Pizza.objects.all()
    pastas_list = Pasta.objects.all()
    salads_list = Salad.objects.all()
    platters_list = Platter.objects.all()
    print(salads_list)

    context = {
        "user": request.user,
        "pizzas": pizzas_list,
        "pastas":pastas_list,
        "salads":salads_list,
        "platters":platters_list,

    }
    
    return render(request, "orders/menu.html", context)


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




""" def index(request):
    context = {
        "Pastas": Pasta.objects.all()
    }
    return render(request, "orders/index.html", context)

def pizza(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk=pizza_id)
    except Pizza.DoesNotExist:
        raise Http404("Pizza does not exist.")
    context = {
        "pizza": pizza
    }
    return render(request, "orders/pizza.html", context) """