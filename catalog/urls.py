from django.urls import path

from catalog.views import index, index_contacts

urlpatterns = [
    path('', index),
    path('', index_contacts),
]