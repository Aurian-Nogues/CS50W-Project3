from django.urls import path
from . import views
from django.contrib import admin





urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_account", views.createAccount, name="create_account"),

]



""" urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pizza_id>", views.pizza, name="pizza")

]
 """