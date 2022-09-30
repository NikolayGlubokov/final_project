from django.db import models


class CategoryParts(models.Model):
    name_category = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Car(models.Model):
    name_car = models.CharField(verbose_name='Название автомобиля')

    def __str__(self):
        return self.name_car

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class SchemePart(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название схемы')
    category = models.ForeignKey(CategoryParts, verbose_name='Категория запчастей')
    image = models.ImageField(upload_to='/media/scheme', verbose_name='Изображение схемы')
    car = models.ForeignKey(Car, verbose_name='Автомобиль')


    def __str__(self):
        return self.num_scheme

    class Meta:
        verbose_name = 'Схема запчастей'
        verbose_name_plural = 'Схемы запчастей'


class Parts(models.Model):
    num_scheme = models.ForeignKey(SchemePart, verbose_name='Номер схемы')
    num_parts = models.CharField()
