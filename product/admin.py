from django.contrib import admin
from .models import Category, Product, ProductImage, Client


class ProductImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  
    list_filter = ('name',) 
    prepopulated_fields = {"slug":("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'merchant', 'category', 'price', 'discount', 'price_before_discount', 'available', 'created', 'updated', 'overview', 'details', 'video')
    list_filter = ("category", "discount", "merchant")
    list_editable = ("price", "available")
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        ProductImageInline
    ]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand_name', 'terms_conditions', 'has_delivery', 'address', 'facebook_link', 'email', 'mobile_number', 'commission', 'created', 'updated')
    list_filter = ('has_delivery', 'created', 'updated')
    search_fields = ('name', 'brand_name')
