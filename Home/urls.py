from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home-home"),
    path("register/", views.register, name="Home-register"),
]