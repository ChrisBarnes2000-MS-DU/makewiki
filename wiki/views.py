from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.shortcuts import render

from wiki.forms import PageForm
from wiki.models import Page

def logout_view(request):
    logout(request)
    # Redirect to a success page.

class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {'pages': pages})

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {'page': page})

class PageCreateView(FormView):
    template_name = 'create.html'
    from_class = PageForm
    success_url = '/'

    def post(self, request):
        pass
