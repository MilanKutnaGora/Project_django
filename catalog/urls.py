from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, index_contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', index_contacts, name='index_contact'),
    path('shop/', ProductListView.as_view(), name='index_shop'),
    path('shop/product/<int:pk>/', ProductDetailView.as_view(), name='index_product'),
]