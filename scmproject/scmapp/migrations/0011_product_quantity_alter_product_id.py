# Generated by Django 4.2 on 2023-05-06 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0010_remove_product_quantity_product_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
