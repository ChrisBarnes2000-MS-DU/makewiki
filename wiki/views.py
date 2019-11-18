from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import render
from django.utils import timezone

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

    def get(self, request, *args, **kwargs):
        context = {'form': PageForm()}
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.published_date = timezone.now()
            page.save()
            return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[page.slug]))
        return render(request, 'create.html', {'form': form})
