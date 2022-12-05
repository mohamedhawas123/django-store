from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static
from .views import cart, add_cart, remove_item, removecartitem


urlpatterns = [
    path("",cart, name='cart' ),
    path("addtocart/<product_id>", add_cart, name="addtocart" ),
    path("removefromcart/<product_id>", remove_item, name="removefromcart" ),
    path("removecartitem/<product_id>", removecartitem, name="removecartitem" ),

   
]
