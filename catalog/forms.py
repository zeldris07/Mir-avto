from .models import Order
from django import forms


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('address', 'number', 'orient')