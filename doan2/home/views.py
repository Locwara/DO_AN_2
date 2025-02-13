from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Cleaned data:", form.cleaned_data) 
            if form.cleaned_data['password'] != form.cleaned_data['rpassword']:
                messages.error(request, 'Mật khẩu không khớp!')
                
                return render (request, 'home/register.html', {'form':form})
            
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Đăng ký thành công!')
            return redirect('login')
        else:
            print("Form errors:", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form': form})

def login(request):
    return render(request, 'home/login.html')