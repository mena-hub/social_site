from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Page

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'ordering']
    success_url = reverse_lazy('pages:pages')

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')