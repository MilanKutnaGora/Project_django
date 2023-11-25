from django.shortcuts import render

def index(request):
    return render(request, 'catalog/home.html', )

def index_contacts(request):
    return render(request, 'catalog/contacts.html')
