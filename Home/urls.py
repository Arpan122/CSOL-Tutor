from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="Home-home"),
    path("register/", views.register, name="Home-register"),
    path("login/", auth_views.LoginView.as_view(template_name='Home/login.html'), name="Home-login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='Home/logout.html'), name="Home-logout"),
]