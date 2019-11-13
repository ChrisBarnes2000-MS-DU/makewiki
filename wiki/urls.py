from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView
from wiki.forms import PageForm

urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PageCreateView.as_view(), name='wiki-create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
