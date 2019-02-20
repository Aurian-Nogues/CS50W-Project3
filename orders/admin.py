from django.contrib import admin
from .models import Pasta, Flavour, Size, ToppingType

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Flavour)
admin.site.register(Size)
admin.site.register(ToppingType)

