from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('trangchu')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password=password)
            
            
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'trangchu')
                return redirect(next_url)
        else:
            form = LoginForm()
        return render(request, 'home2/dangnhap.html', {'form': form})