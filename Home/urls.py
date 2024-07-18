from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home-home"),
    path("login/", views.login, name="Home-login"),
]