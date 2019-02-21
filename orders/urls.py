from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]




""" urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pizza_id>", views.pizza, name="pizza")

]
 """