from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('update/', views.update_cart, name='update_cart')
]
