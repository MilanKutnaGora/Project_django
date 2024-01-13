from django.contrib.auth.models import AbstractUser
from django.db import models
import random

NULLABLE = {'blank': True, 'null': True}

random_code = str(random.randint(00000000, 99999999))

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    # verification_code = models.CharField(max_length=8, default=random_code,
    #                                      verbose_name='код подтверждения почты', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
