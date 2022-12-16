from django.shortcuts import render
from django.http import HttpResponse
from pro.models import Product
from core.models import Category
from cart.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from pro.models import Variation
from django.contrib.auth.models import User


def home(request):

    user = User()
    if user is not None:
        print(User.first_name)
    else:
        print("donest exist")
    products = Product.objects.all().filter(is_avaliabel=True)
    
    return render(request, 'core/home.html', {'products': products})



def store(request, slug=None):
    products = None
    if slug:
        products = Product.objects.all().filter(category=slug)
        pagin= Paginator(products, 3)
        page = request.GET.get('page')
        page_product = pagin.get_page(page)
    else:

        products = Product.objects.all().filter(is_avaliabel=True).order_by('id')
        pagin= Paginator(products, 3)
        page = request.GET.get('page')
        page_product = pagin.get_page(page)
        print(page_product)
    cate= Category.objects.all()
    s = products.count()
    return render(request, 'core/store.html', {'products': page_product , 's': s, 'categor':cate})



def prduct_detail(request, slug):
    product = Product.objects.get(id=slug)

    size = product.product_variation.all().filter(variation_category='size')
    color = product.product_variation.all().filter(variation_category='color')
    
    
    

    is_exist=  CartItem.objects.filter(product=product).exists()
    return render(request, 'core/product_detail.html', {
        'product': product,'is_exist': is_exist,
        'color':color ,
        'size':size
         })




def search(request):
        keyword = request.GET.get('keyword')
        products= Product.objects.all().filter(product_name__icontains=keyword )
        s = products.count()
            
        return render(request, 'core/store.html', {'products': products, 's': s})

