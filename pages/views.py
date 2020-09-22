from django.shortcuts import render, get_list_or_404
from .models import Page

def pages(request):
    pages = get_list_or_404(Page)
    return render(request, "pages/page_list.html", {'pages': pages})