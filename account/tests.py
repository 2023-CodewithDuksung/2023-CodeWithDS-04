from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    last_name = models.CharField(max_length=30)  # 예시로 추가
    first_name = models.CharField(max_length=30)  # 예시로 추가
