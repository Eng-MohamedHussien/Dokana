from django.contrib import admin

from .models import Order, OrderItem


class InlineOrderItem(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price')
    readonly_fields = ('product', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_name', 'mobile_number', 'another_mobile_number', 'city', 'address', 'created']
    list_filter = ['entered_at_taager', 'delivered_to_customer', 'created', 'updated']
    inlines = [InlineOrderItem]
