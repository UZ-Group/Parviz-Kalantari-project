from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    is_author = models.BooleanField(default=False, verbose_name='وضعیت نویسندگی')
    receive_email = models.BooleanField(default=False, verbose_name='دریافت ایمیل برای هر مقاله جدید')