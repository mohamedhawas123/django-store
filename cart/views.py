from django.shortcuts import render, redirect
from pro.models import Product
from .models import Cart, CartItem, AddressUser
from django.http import HttpResponse
from pro.models import Variation
from django.contrib.auth.decorators import login_required
from .form import AddrssUser



def _card_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    product_varriation = []
    if request.method == 'POST':

        for key, value in request.POST.items():
            try:
                variation = Variation.objects.get(product =product, variation_category__iexact=key, variation_value__iexact=value)
                product_varriation.append(variation)
            except :

                pass
        

 
    try:
        cart= Cart.objects.get(cart_id=_card_id(request))
    except Cart.DoesNotExist:
        cart=  Cart.objects.create(
            cart_id=_card_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if len(product_varriation) > 0:
            for item in product_varriation:

                cart_item.variation.add(item)
        cart_item.quantity +=1
       
        cart_item.save()
    except CartItem.DoesNotExist:

        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,)

        if len(product_varriation) > 0:
            for item in product_varriation:

                cart_item.variation.add(item)
        
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




@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.get(cart_id=_card_id(request))
    items = CartItem.objects.filter(cart=cart) 
    user = request.user 

    for item in items:
        item.user = user 
        item.save()
   

    total_price = 0

    total = 0
    
    for item in items:
        total_price += item.quantity * item.product.price
    return render(request, 'cart/checkout.html', {'items': items})




def place_order(request):
    cart = Cart.objects.get(cart_id=_card_id(request))
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        address = request.POST.get("address")
        order_note = request.POST.get("order_note")
        print(first_name, last_name, email, state, country, phone_number)
        address_user = AddressUser()
        address_user.first_name = first_name
        address_user.last_name = last_name
        address_user.email=email
        address_user.phone_number=phone_number
        address_user.address_line = address
        address_user.city = city
        address_user.state =state
        address_user.country = country
        address_user.order_note = order_note
        address_user.user = request.user 
        address_user.cart = cart
        address_user.save()
        return HttpResponse("well")
    
    else:
        raise ValueError("something went wrong")


        
