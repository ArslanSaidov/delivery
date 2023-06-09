# Generated by Django 4.1.3 on 2023-05-12 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_location_customer_location_establishments_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='establishments',
            name='location',
        ),
        migrations.RemoveField(
            model_name='food',
            name='cd',
        ),
        migrations.AddField(
            model_name='food',
            name='establishment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.establishments'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='establishments',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.foodcategory'),
        ),
    ]
