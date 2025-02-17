from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
# Create your views here.

def trangchu(request):
    return render (request, 'home2/trangchu.html')
def dangnhap(request):
    return render(request, 'home2/dangnhap.html')
def quenmatkhau(request):
    return render(request, 'home2/quenmatkhau.html')
def spdangbang(request):
    return render(request, 'home2/spdangbang.html')
def spdanghienthi(request):
    return render(request, 'home2/spdanghienthi.html')
def quanlysanpham(request):
    return render(request, 'home2/quanlysanpham.html')
def quanlydonhang(request):
    return render(request, 'home2/quanlydonhang.html')
def thongkedoanhso(request):
    return render(request, 'home2/thongkedoanhso.html')
def doimatkhau(request):
    return render(request, 'home2/doimatkhau.html')
