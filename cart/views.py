from django.shortcuts import render, redirect
from pro.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse
from pro.models import Variation


def _card_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):


    product = Product.objects.get(id=product_id)
    try:
        cart= Cart.objects.get(cart_id=_card_id(request))
    except Cart.DoesNotExist:
        cart=  Cart.objects.create(
            cart_id=_card_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:

        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,)
        
        cart_item.save()
    
    # return HttpResponse(cart_item.product)
    return redirect('cart')


def remove_item(request, product_id):
    try:
        cart = Cart.objects.get(cart_id=_card_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_card_id(request))
    cart.save()

    
    cart_item = CartItem.objects.get(product=product_id, cart=cart)
    if cart_item.quantity >0:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
        cart.save()
    return redirect('cart')
    

def removecartitem(request, product_id):
    cart=  Cart.objects.get(cart_id=_card_id(request))
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product_id)
        cart_item.delete()
        cart.save()
    except CartItem.DoesNotExist:
        return HttpResponse("Does not Exist")
    
    return redirect('cart')



def cart(request):
    
        
    cart = Cart.objects.get(cart_id=_card_id(request))
   
    items = CartItem.objects.filter(cart=cart)
    # print(cart.cartitem_cart.count())


    total_price = 0

    total = 0
    
    for item in items:
        total_price += item.quantity * item.product.price
        
    
    return render(request, 'cart/carty.html', {'items': items, 'total':total_price, 'cart_item':items })