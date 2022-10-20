from django.db import models
from users.models import User


class CategoryParts(models.Model):
    name_category = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Car(models.Model):
    name_car = models.CharField(max_length=250, verbose_name='Название автомобиля', blank=True)

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class SchemePart(models.Model):
    num_scheme = models.CharField(max_length=255, verbose_name='Номер схемы')
    name = models.CharField(max_length=255, verbose_name='Название схемы')
    category = models.ForeignKey(CategoryParts, verbose_name='Категория запчастей', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/scheme', verbose_name='Изображение схемы', blank=True)
    car = models.ForeignKey(Car, verbose_name='Автомобиль', on_delete=models.CASCADE)

    def __str__(self):
        return self.num_scheme

    class Meta:
        verbose_name = 'Схема запчастей'
        verbose_name_plural = 'Схемы запчастей'


class Parts(models.Model):
    num_scheme = models.ForeignKey(SchemePart, verbose_name='Номер схемы', on_delete=models.CASCADE)
    num_parts = models.CharField(max_length=100, verbose_name='Номер запчасти на схеме')
    articul = models.CharField(max_length=200, verbose_name='Артикул запчасти')
    name = models.CharField(max_length=200, verbose_name='Название запчасти')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


class Journal(models.Model):
    num_scheme = models.ForeignKey(SchemePart, verbose_name='Номер схемы', on_delete=models.CASCADE)
    num_parts = models.CharField(max_length=100, verbose_name='Номер запчасти на схеме')
    articul = models.CharField(max_length=200, verbose_name='Артикул запчасти')
    name = models.CharField(max_length=200, verbose_name='Название запчасти')
    price = models.IntegerField(verbose_name='Стоимость')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    users = models.ForeignKey(User, on_delete=models.CASCADE)
