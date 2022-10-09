# Generated by Django 4.0.5 on 2022-10-05 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_car', models.CharField(max_length=250, verbose_name='Название автомобиля')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='CategoryParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SchemePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название схемы')),
                ('image', models.ImageField(upload_to='media/scheme', verbose_name='Изображение схемы')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.car', verbose_name='Автомобиль')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.categoryparts', verbose_name='Категория запчастей')),
            ],
            options={
                'verbose_name': 'Схема запчастей',
                'verbose_name_plural': 'Схемы запчастей',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_parts', models.CharField(max_length=100, verbose_name='Номер запчасти на схеме')),
                ('articul', models.CharField(max_length=200, verbose_name='Артикул запчасти')),
                ('name', models.CharField(max_length=200, verbose_name='Название запчасти')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.categoryparts', verbose_name='Категория')),
                ('num_scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoparts.schemepart', verbose_name='Номер схемы')),
            ],
            options={
                'verbose_name': 'Деталь',
                'verbose_name_plural': 'Детали',
            },
        ),
    ]