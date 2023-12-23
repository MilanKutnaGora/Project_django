from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from record.models import Record


class RecordCreateView(CreateView):
    model = Record
    fields = ('name', 'description',)
    success_url = reverse_lazy('record:list')

class RecordUpdateView(UpdateView):
    model = Record
    fields = ('name', 'description',)
    success_url = reverse_lazy('record:list')

class RecordListView(ListView):
    model = Record

class RecordDetailView(DetailView):
    model = Record

class RecordDeleteView(DeleteView):
    model = Record
    success_url = reverse_lazy('record:list')