from django.contrib import admin
from django.urls import path
from core.views import home, store
from django.conf import  settings
from django.conf.urls.static import static


urlpatterns = [
    path("",home, name='home' ),
    path("store",store, name="store" ),
    path("store/<slug:slug>",store, name="store_slug" )
]


