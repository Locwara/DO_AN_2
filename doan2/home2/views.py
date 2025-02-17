from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
# Create your views here.

def trangchu(request):
    return render (request, 'home2/trangchu.html')
