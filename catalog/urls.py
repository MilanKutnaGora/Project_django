from django.urls import path

from catalog.views import index, index_contacts, index_shop

urlpatterns = [
    path('', index),
    path('contacts/', index_contacts),
    path('shop/', index_shop)
]