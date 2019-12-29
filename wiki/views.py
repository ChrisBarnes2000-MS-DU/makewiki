from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from wiki.forms import PageForm
from wiki.models import Page

def logout_view(request):
    logout(request)
    # Redirect to a success page.

class PageListView(ListView):
    template_name = 'wiki/list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

class PageDetailView(DetailView):
    model = Page
    template_name = 'wiki/page.html'

class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content']

class PageEditView(UpdateView):
    model = Page
    fields = ['title', 'content']

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('wiki-list-page')