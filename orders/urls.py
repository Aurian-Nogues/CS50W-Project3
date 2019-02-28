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
    path("cart", views.cart, name="cart"),
    path("toppings/<str:description>/<str:topping>/<str:price>", views.pizza_toppings, name="toppings"),
    path("subs_extras/<str:description>/<str:size>/<str:price>", views.subs_extras, name="subs_extras"),
    path("add_pasta_salad/<str:description>/<str:price>", views.add_pasta_salad, name="add_pasta_salad"),
    path("add_platter/<str:description>/<str:size>/<str:price>", views.add_platter, name="add_platter"),
    path("add_pizza", views.add_pizza, name="add_pizza"),
    path("add_sub", views.add_sub, name="add_sub"),
    path("delete_item", views.delete_item, name="delete_item"),
    path("confirm_order", views.confirm_order, name="confirm_order"),
    path("staff_confirmed_orders", views.staff_confirmed_orders, name="staff_confirmed_orders"),
    path("staff_all_orders", views.staff_all_orders, name="staff_all_orders"),
    path("update_order", views.update_order, name="update_order"),
    path("staff_see_orders/<str:order_number>", views.staff_see_orders, name="staff_see_orders"),
]

