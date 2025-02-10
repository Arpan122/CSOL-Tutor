from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def acsl(request):
    return render(request, "Tutor/acsl/index.html")