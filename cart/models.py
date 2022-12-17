from django.db import models
from pro.models import Product, Variation
from accounts.models import Account

class Cart(models.Model):
    cart_id= models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.cart_id)





class CartItem(models.Model):
    user= models.ForeignKey(Account, related_name='cart_user' ,on_delete=models.CASCADE, blank=True, null=True)
    variation = models.ManyToManyField(Variation, blank=True)

    product=models.ForeignKey(Product, related_name='cart_product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cartitem_cart', blank=True, null=True ,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    is_active = models.BooleanField(default=True)

    def get_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return self.product.product_name




class AddressUser(models.Model):
    cart = models.ForeignKey(Cart, related_name='user_cart', blank=True, null=True ,on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='user_addrss', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=245)
    last_name = models.CharField(max_length=245)
    email = models.EmailField(max_length=245)
    phone_number = models.CharField(max_length=245)
    address_line = models.CharField(max_length=245)
    city = models.CharField(max_length=245)
    state = models.CharField(max_length=245)
    country = models.CharField(max_length=245)
    order_note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name