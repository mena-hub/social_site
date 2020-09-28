from django.urls import path
from pages.views import PageListView, PageDetailView, PageCreateView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name="page"),
    path('create/', PageCreateView.as_view(), name="create"),
], 'pages')