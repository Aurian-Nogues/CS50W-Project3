from django.http import HttpResponse
from django.shortcuts import render
from .models import Pasta

# Create your views here.
def index(request):
    context = {
        "Pastas": Pasta.objects.all()
    }
    return render(request, "orders/index.html", context)
