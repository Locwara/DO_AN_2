
from django.urls import path
from . import views as home
urlpatterns = [
    path('register/', home.register, name='register'),
    path('login/', home.login, name='login'),
]