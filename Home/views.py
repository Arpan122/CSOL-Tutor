from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now login.')
            return redirect('Home-login')
    else:
        form = UserRegisterForm()
    return render(request, "Home/register.html", {'form': form})

#Custom Login view
def customLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('Home-dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, "Home/login.html", {'form': form})

@login_required
def customLogout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('Home-home')

@login_required
def dashboard(request):
    return render(request, "Home/dashboard.html")