from rest_framework import generics

from wiki.models import Page
from .serializer import PageSerializer

class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(generics.RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
