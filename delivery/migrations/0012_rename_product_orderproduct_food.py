# Generated by Django 4.1.3 on 2023-05-18 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_order_rename_product_cartitem_food_orderproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='product',
            new_name='food',
        ),
    ]
