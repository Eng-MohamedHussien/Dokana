from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, Category, ProductImage
from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')


def open_dokana(request):
    return render(request, 'open_dokana.html')


def show_category_items(request, category_slug):
    selected_category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=selected_category, available=True).order_by('created')
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'category_products.html', {'products': page_obj, 'selected_category': selected_category, 'title': f"دكانه | {selected_category.name}", 'num_pages': [i + 1 for i in range(paginator.num_pages)]})


def product_details(request, product_slug):
    selected_product = get_object_or_404(Product, slug=product_slug, available=True)
    album = ProductImage.objects.filter(product__slug=product_slug)
    return render(request, 'product_details.html', {'product': selected_product, 'album': album, 'title': f"دكانه | {selected_product.name}"})


def show_discounts(request):
    products = Product.objects.filter(available=True, discount=True).order_by('created')
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'category_discounts.html', {'products': page_obj, 'title': f"دكانه | خصومات و عروض", 'num_pages': [i + 1 for i in range(paginator.num_pages)]})


def show_discounts_per_category(request, category_slug):
    selected_category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=selected_category, available=True, discount=True).order_by('created')
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'category_discounts.html', {'products': page_obj, 'selected_category': selected_category, 'title': f"دكانه | خصومات و عروض {selected_category.name}", 'num_pages': [i + 1 for i in range(paginator.num_pages)]})