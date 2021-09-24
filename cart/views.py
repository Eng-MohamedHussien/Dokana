from django.shortcuts import render
from .cart import Cart
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from product.models import Product


def add_to_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('id', None)
        quantity = data.get('quantity', None)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, quantity)
        return JsonResponse({'status': 'success'}, status=201)


def remove_from_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('id', None)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return JsonResponse({'status': 'success'}, status=201)


def cart_detail(request):
    return render(request, 'cart_detail.html', {'title': 'دكانه | عربة التسوق'})


def update_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('id', None)
        quantity = data.get('quantity', None)
        product = get_object_or_404(Product, id=product_id)
        cart.update(product, quantity)
        return JsonResponse({'status': 'success'}, status=201)
