from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static
from .views import login, register, logout



urlpatterns = [
    
    path("/login", login, name='login'),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout")

   
]

print(urlpatterns)