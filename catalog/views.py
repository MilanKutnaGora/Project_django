from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'catalog/home.html', )

def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

def index_shop(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        }
    return render(request, 'catalog/shop.html', context)

def index_product(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
        }

    return render(request, 'catalog/product.html', context)
