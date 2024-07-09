from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='урок'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='описание'
    )
    preview = models.ImageField(
        upload_to='materials/lesson/preview',
        blank=True,
        null=True,
        verbose_name='превью'
    )
    video = models.ImageField(
        upload_to='materials/lesson/video',
        blank=True,
        null=True,
        verbose_name='видео'
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='курс'
    )
    preview = models.ImageField(
        upload_to='materials/course/preview',
        blank=True,
        null=True,
        verbose_name='превью'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='описание'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name='урок',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='название курса'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        unique_together = ('user', 'course')

