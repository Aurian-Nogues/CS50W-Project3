from django.urls import path
from . import views
from django.contrib import admin





urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_account", views.createAccount, name="create_account"),
    path("pizzas", views.pizzas, name="pizzas"),
    path("subs", views.subs, name="subs"),
    path("pastas", views.pastas, name="pastas"),
    path("salads", views.salads, name="salads"),
    path("platters", views.platters, name="platters"),
    path("toppings/<str:description>/<str:topping>/<str:price>", views.pizza_toppings, name="toppings"),
    path("subs_extras/<str:description>/<str:size>/<str:price>", views.subs_extras, name="subs_extras"),
    path("add_pizza", views.add_pizza, name="add_pizza"),
    path("add_sub", views.add_sub, name="add_sub"),

]

