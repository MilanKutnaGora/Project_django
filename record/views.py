from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from record.models import Record


class RecordCreateView(CreateView):
    model = Record
    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:index_shop')

class RecordListView(ListView):
    model = Record
