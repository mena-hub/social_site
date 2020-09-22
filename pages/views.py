from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Page

def pages(request):
    pages = get_list_or_404(Page)
    return render(request, "pages/page_list.html", {'pages': pages})

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, "pages/page_detail.html", {'page':page})