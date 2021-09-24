# Generated by Django 3.2.5 on 2021-09-16 16:00

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='design',
            field=models.ImageField(blank=True, null=True, upload_to=product.models.generate_category_image_path, verbose_name='صورة تسويقية للصنف'),
        ),
    ]