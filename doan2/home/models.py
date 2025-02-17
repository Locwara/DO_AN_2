from django.db import models
# import Abs va Per để có thể dùng cách hàm có Django có sẵn
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
# import hàm make_password của django
from django.contrib.auth.hashers import make_password
# Create your models here.


# Tạo một model UserClient kế thừa từ models của django
class UserClient(models.Model):
    # Khỏi tạo cách biến bằng cách trường tương ứng có trong table trong database
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=255)
    auth_type = models.CharField(max_length=20, choices=[('email', 'Email'), ('facebook', 'Facebook'), ('tranditional', 'Tranditional')], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    # hàm xác thực luôn trả về true :)))
    @property
    def is_authenticated(self):
        return True
    # lớp Meta dùng để liên kết với table users trong database
    class Meta:
        db_table = 'users'
    # Hàm set_password làm thủ công do django không hỗ trợ
    def set_password(self, raw_password):
        # make_password để mã hóa mật khẩu
        self.password = make_password(raw_password)
     
     
     

         
         