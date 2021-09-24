# Generated by Django 3.2.5 on 2021-09-17 16:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_category_discount_design'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='اسم التاجر')),
                ('brand_name', models.CharField(max_length=256, verbose_name='اسم الصفحة او المحل')),
                ('terms_conditions', models.TextField(verbose_name='شروط و احكام استرجاع المنتج')),
                ('has_delivery', models.BooleanField(default=True, verbose_name='خدمة توصيل')),
                ('address', models.CharField(max_length=256, verbose_name='عنوانه او عنوان محله')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='لينك لصفحة الفيسبوك')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='البريد الالكترونى')),
                ('mobile_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='([0]{1}[1]{1}[0-9]{9})')], verbose_name='رقم المحمول')),
                ('another_mobile_number', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(regex='([0]{1}[1]{1}[0-9]{9})')], verbose_name='الرقم البديل')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='توقيت الاضافة')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='توقيت اخر تعديل')),
            ],
            options={
                'verbose_name': 'تاجر',
                'verbose_name_plural': 'تجار',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.client', verbose_name='المورد'),
        ),
    ]
