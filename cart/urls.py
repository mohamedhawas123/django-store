from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static
from .views import cart, add_cart, remove_item, removecartitem, checkout, place_order


urlpatterns = [
    path("",cart, name='cart' ),
    path("addtocart/<product_id>", add_cart, name="addtocart" ),
    path("removefromcart/<product_id>", remove_item, name="removefromcart" ),
    path("removecartitem/<product_id>", removecartitem, name="removecartitem" ),
    path("checkout", checkout, name="checkout"),
    path("place_order", place_order, name="place_order"),


   
]
