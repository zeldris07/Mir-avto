
from django import template
from cart.cart import Cart

register = template.Library()


@register.simple_tag(takes_context=True)
def cart_total_amount(context):
    request = context['request']
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0.0
        for key,value in request.session['cart'].items():
            total_bill = total_bill + (float(value['price']) * value['quantity'])
        return total_bill
    else:
        return 0