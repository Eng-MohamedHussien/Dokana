# Generated by Django 3.2.5 on 2021-09-12 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210910_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='السعر / السعر بعد الخصم'),
        ),
    ]
