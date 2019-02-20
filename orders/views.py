from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Pasta, Pizza

# Create your views here.
def index(request):
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
    return render(request, "orders/pizza.html", context)