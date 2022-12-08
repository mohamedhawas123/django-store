from .views import _card_id
from .models import CartItem, Cart

def menu_linkess(request):
    cart_count = 0
    try:
        cart = Cart.objects.filter(cart_id=_card_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart[:1])
        for item in cart_items:
            cart_count += item.quantity
    except Cart.DoesNotExist:
        cart_count = 0  


    return dict(cart_count=cart_count)
