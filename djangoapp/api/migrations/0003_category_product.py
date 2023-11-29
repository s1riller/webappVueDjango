# Generated by Django 4.2.7 on 2023-11-24 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='Количество на складе')),
                ('is_prescription_required', models.BooleanField(default=False, verbose_name='Требуется рецепт')),
                ('size', models.CharField(blank=True, max_length=20, null=True, verbose_name='Размер')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Цвет')),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='Бренд')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Модель')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
