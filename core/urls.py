from django.contrib import admin
from django.urls import path
from core.views import home, store, prduct_detail, search
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path("",home, name='home' ),
    path("store",store, name="store" ),
    path("store/<slug:slug>",store, name="store_slug" ),
    path("product_detail/<slug:slug>", prduct_detail, name="prduct_detail" ),
    path("search", search, name="search")
]


