
from django.urls import path
from . import views as home
urlpatterns = [
    # đường dẫn cho trang đăng nhập
    path('login/', home.login_view, name="login"),
    # đường dẫn cho trang chủ
    path('trangchu/', home.trangchu, name="trangchu")
]