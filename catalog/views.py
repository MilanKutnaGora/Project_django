from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/home.html')

def index_contacts(request):
    return render(request, 'catalog/contacts.html')

def index_shop(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/shop.html', context)
