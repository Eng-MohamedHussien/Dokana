from django import forms
from .models import Order


class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['owner_name', 'mobile_number', 'another_mobile_number', 'city', 'address']