from django.conf import settings
from decimal import Decimal
from product.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if cart is None:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}  
            self.save()

    def update(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.cart.keys():
            self.cart[product_id]['quantity'] = quantity
            self.save()

    def save(self):
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['quantity'] * Decimal(item['price']) for item in self.cart.values())

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart.keys():
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    