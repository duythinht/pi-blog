from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Entry


class EntryListView(ListView):
    model = Entry
    paginate_by = 10


class TagView(ListView):
    model = Entry
    paginate_by = 10

    def get_queryset(self):
        tag = self.kwargs['tag']
        return self.model.objects.filter(tags__contains=tag)


class EntryDetailView(DetailView):
    model = Entry