import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


def index(request):
    return render(request, 'catalog/home.html', )

def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/shop.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

def index_product(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{category_item.name}'
        }

    return render(request, 'catalog/product.html', context)



class ProductCreateView(LoginRequiredMixin, CreateView):
   model = Product
   form_class = ProductForm
   success_url = reverse_lazy('catalog:index_shop')

   def form_valid(self, form):
       if form.is_valid():
           new_contact = form.save()
           new_contact.personal_manager = self.request.user
           new_contact.save()
           contact_dict = {
               "Имя": new_contact.contact_name,
               "Почта": new_contact.contact_email
           }
           with open("contacts.json", 'a', encoding='UTF-8') as f:
               json.dump(contact_dict, f, indent=2, ensure_ascii=False)
       return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index_shop')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1,)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if form.is_valid():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)


