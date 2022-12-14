from django.db import models
from core.models import Category
from django.urls import reverse


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


    def get_url(self):
        return reverse('prduct_detail', args=[self.id])

    def __str__(self):
        return self.product_name

variation_category_choice = (
    ('color', 'color'),
    ('size', 'size')
)


class Variation(models.Model):
    product = models.ForeignKey(Product, related_name='product_variation', on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=244, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name

        