# Generated by Django 3.2.5 on 2021-09-16 23:26

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_design'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='discount_design',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.generate_category_image_path, verbose_name='صورة خصومات للصنف'),
        ),
    ]