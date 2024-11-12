from django.db import models

# Create your models here.

class Contacts(models.Model):

    TARIFF_CHOICES = [
        ('basic', 'Базовый — 29 900 тг/месяц'),
        ('advanced', 'Продвинутый — 49 900 тг/месяц'),
        ('premium', 'Премиум — 79 900 тг/месяц'),
    ]

    name = models.CharField(max_length=255, verbose_name='Имя')
    city = models.CharField(max_length=255, verbose_name='Город')
    tariff = models.CharField(max_length=50, choices=TARIFF_CHOICES, verbose_name='Тарифный план')
    email = models.EmailField(max_length=255, verbose_name='email')
    number = models.CharField(max_length=50, verbose_name='Номер')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['time_create']


class Opens(models.Model):
    ip = models.CharField(max_length=255, verbose_name='IP')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Количество открытий'
        verbose_name_plural = 'Количество открытий'
        ordering = ['time_create']