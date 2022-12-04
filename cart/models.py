from django.db import models
from pro.models import Product

class Cart(models.Model):
    cart_id= models.CharField(max_length=250, blank=True)
    date_add = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.cart_id





class CartItem(models.Model):
    product=models.ForeignKey(Product, related_name='cart_product', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cartitem_cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.product
