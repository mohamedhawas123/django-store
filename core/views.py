from django.shortcuts import render
from django.http import HttpResponse
from pro.models import Product
from core.models import Category


def home(request):

    products = Product.objects.all().filter(is_avaliabel=True)
    print(products)
    return render(request, 'core/home.html', {'products': products})



def store(request, slug=None):
    products = None
    if slug:
        products = Product.objects.all().filter(category=slug)
    else:

        products = Product.objects.all().filter(is_avaliabel=True)
    cate= Category.objects.all()
    s = products.count()
    return render(request, 'core/store.html', {'products': products, 's': s, 'categor':cate})