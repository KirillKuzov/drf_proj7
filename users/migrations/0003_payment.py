# Generated by Django 5.0.6 on 2024-06-30 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True, verbose_name='дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма оплаты')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('card', 'Карта')], max_length=20, verbose_name='способ оплаты')),
                ('session_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID сессии')),
                ('link', models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='оплаченный курс')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.lesson', verbose_name='отдельно оплаченный урок')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'платеж',
                'verbose_name_plural': 'платежи',
            },
        ),
    ]