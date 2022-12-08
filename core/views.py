from django.shortcuts import render
from django.http import HttpResponse
from pro.models import Product
from core.models import Category
from cart.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



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
        pagin= Paginator(products, 3)
        page = request.GET.get('page')
        page_product = pagin.get_page(page)
        print(page_product)
    cate= Category.objects.all()
    s = products.count()
    return render(request, 'core/store.html', {'products': page_product , 's': s, 'categor':cate})



def prduct_detail(request, slug):
    product = Product.objects.get(id=slug)
    is_exist=  CartItem.objects.filter(product=product).exists()
    return render(request, 'core/product_detail.html', {'product': product, 'is_exist': is_exist })