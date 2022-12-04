from django.db import models
from core.models import Category


class Product(models.Model):
    product_name  = models.CharField(max_length=200)
    slug  = models.SlugField()
    description  = models.TextField(max_length=200, blank=True, null=True)
    price  = models.IntegerField()
    images  = models.ImageField(upload_to='products')
    stock  = models.IntegerField()
    is_avaliabel = models.BooleanField(default=True)
    category=  models.ForeignKey(Category, related_name='category_product', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_data = models.DateTimeField(auto_now=True)