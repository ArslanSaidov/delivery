# Generated by Django 4.2 on 2023-04-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('food_category', models.CharField(blank=True, choices=[('Закуски', 'Закуски'), ('Первые блюда', 'Первые блюда'), ('Вторые блюда', 'Вторые блюда'), ('Салаты', 'Салаты'), ('Десерты', 'Десерты'), ('Пицца', 'Пицца'), ('Fast food', 'Fast food'), ('Напитки', 'Напитки'), ('Алкоголь', 'Алкоголь')], max_length=255, null=True)),
            ],
        ),
    ]
