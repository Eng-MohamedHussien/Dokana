from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid() and len(cart) != 0:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return redirect('order:order_created')
        elif len(cart) == 0:
            return redirect('cart:cart_detail')
    else:
        form = CreateOrderForm()
    
    return render(request, 'create_order.html', {'form': form, 'title': 'دكانه | سجل الاوردر'})


def order_created(request):
    return render(request, 'order_created.html', {'title': 'دكانه | تم تسجيل طلبك بنجاح'})