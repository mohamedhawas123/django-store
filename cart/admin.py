from django.contrib import admin
from .models import Cart, CartItem, AddressUser

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(AddressUser)