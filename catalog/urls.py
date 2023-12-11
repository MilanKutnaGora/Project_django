from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, index_contacts, index_shop




app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', index_contacts, name='index_contact'),
    path('shop/', index_shop, name='index_shop')
]