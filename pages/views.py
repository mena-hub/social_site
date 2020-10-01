from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'ordering']
    success_url = reverse_lazy('pages:pages')

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return self.object.get_absolute_url() + '?ok'