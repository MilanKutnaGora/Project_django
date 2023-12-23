from django.urls import path
from record.apps import RecordConfig
from catalog.views import index, index_contacts, ProductListView, ProductDetailView
from record.views import RecordCreateView, RecordListView

app_name = RecordConfig.name

urlpatterns = [
    path('create/', RecordCreateView.as_view(), name='create'),
    path('', RecordListView.as_view(), name='list'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),

]
