from django.db import models
from django.core.validators import RegexValidator

from product.models import Product


class Order(models.Model):
    owner_name = models.CharField(max_length=128, verbose_name='الاسم بالكامل')
    mobile_number_regex = RegexValidator(regex=r"([0]{1}[1]{1}[0-9]{9})")
    mobile_number = models.CharField(max_length=11, verbose_name='رقم المحمول', validators=[mobile_number_regex]) 
    another_mobile_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='الرقم البديل', validators=[mobile_number_regex])
    city = models.CharField(max_length=64, verbose_name='المحافظة')
    address = models.CharField(max_length=512, verbose_name='العنوان بالتفصيل(المنطقة, اسم الشارع, رقم العقار , رقم الشقة)')
    entered_at_taager = models.BooleanField(default=False, verbose_name='تم تسجيله على منصة التسويق بالعمولة')
    delivered_to_customer = models.BooleanField(default=False, verbose_name='تم استلام المنتج') 
    created = models.DateTimeField(auto_now_add=True, verbose_name='توقيت التسجيل')
    updated = models.DateTimeField(auto_now=True, verbose_name='توقيت اخر تعديل')

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('-created',)
        verbose_name = "اوردر"
        verbose_name_plural = "اوردرات"

    def get_order_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_order_quantities(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name='اسم المنتج')
    quantity = models.PositiveIntegerField(default=1, verbose_name='الكمية')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='السعر')

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.quantity * self.price