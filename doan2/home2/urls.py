
from django.urls import path
from . import views as home
urlpatterns = [
    # đường dẫn cho trang đăng nhập
    path('login/', home.login_view, name="login"),
    # đường dẫn cho trang chủ
    path('trangchu/', home.trangchu, name="trangchu"),
    path('quenmatkhau/', home.quenmatkhau, name='quenmatkhau'),
    path('spdangbang/', home.spdangbang, name='spdangbang'),
    path('spdanghienthi/', home.spdanghienthi, name='spdanghienthi'),
    path('quanlysanpham/', home.quanlysanpham, name='quanlysanpham'),
    path('quanlydonhang/', home.quanlydonhang, name='quanlydonhang'),
    path('thongkedoanhso/', home.thongkedoanhso, name='thongkedoanhso'),
    path('doimatkhau/', home.doimatkhau, name='doimatkhau'),
]