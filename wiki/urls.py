from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView, PageEditView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PageCreateView.as_view(), name='wiki-create-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('<str:slug>/edit/', PageEditView.as_view(), name='wiki-edit-page'),
    path('<str:slug>/delete/', PageDeleteView.as_view(), name='wiki-delete-page'),
]
