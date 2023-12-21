from django.urls import path
from records.apps import RecordConfig
from catalog.views import index, index_contacts, ProductListView, ProductDetailView

app_name = RecordConfig.name

urlpatterns = [
    path('create/', ..., name='create'),
    path('', ..., name='list'),
    path('view/<int:pk>/', ..., name='view'),
    path('edit/<int:pk>/', ..., name='edit'),
    path('delete/<int:pk>/', ..., name='delete'),

]
