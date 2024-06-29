from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='почта',
        help_text='укажите почту'
    )
    phone = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name='телефон',
        help_text='укажите телефон'
    )
    city = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='город',
        help_text='укажите свой город'
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        blank=True,
        null=True,
        verbose_name='аватар',
        help_text='загрузите свой аватар'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи'
