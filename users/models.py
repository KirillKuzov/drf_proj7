from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}
PAYMENT_METHOD_CHOICES = (
    ('cash', 'Наличные'),
    ('card', 'Карта'),
)


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


class Payment(models.Model):
    objects = None
    from materials.models import Course, Lesson
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='отдельно оплаченный урок', **NULLABLE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')
    # session_id = models.CharField(max_length=255, verbose_name="ID сессии", **NULLABLE)
    # link = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f'{self.user} - оплачено {self.course}, {self.lesson}.'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
