from django.contrib import admin
from .models import Category
from pro.models import Variation


admin.site.register(Category)
admin.site.register(Variation)