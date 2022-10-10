from datetime import datetime

from django.db import models


class Color(models.Model):
    color = models.CharField('цвет', max_length=250, unique=True)

    def __str__(self):
        return self.color


class Mark(models.Model):
    mark = models.CharField('марка автомобиля', max_length=250, unique=True)

    def __str__(self):
        return self.mark


class Auto(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='autos', verbose_name='марка')
    model = models.CharField('модель автомобиля', max_length=250, unique=True)

    def __str__(self):
        return f'{self.mark} {self.model}'


class Order(models.Model):
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, related_name='orders', verbose_name='цвет')
    auto = models.ForeignKey(Auto, on_delete=models.DO_NOTHING, related_name='orders', verbose_name='модель автомобиля')
    auto_count = models.PositiveIntegerField('количество автомобилей')
    created = models.DateTimeField(default=datetime.now(), blank=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.auto}, {self.auto_count}, {self.color}'
