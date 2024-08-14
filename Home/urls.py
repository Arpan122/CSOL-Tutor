from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="Home-home"),
    path("register/", views.register, name="Home-register"),
    path("login/", views.customLogin, name="Home-login"),
    path("logout/", views.customLogout, name="Home-logout"),
    path("dash/", views.dashboard, name="Home-dashboard")
]