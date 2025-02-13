from .models import UserClient
from django import  forms
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)
    
    class Meta: 
        model = UserClient
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password']    