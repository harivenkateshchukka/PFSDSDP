# Generated by Django 4.2 on 2023-05-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='Customer_table',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order_table',
        ),
        migrations.AlterModelTable(
            name='product',
            table='product_table',
        ),
    ]