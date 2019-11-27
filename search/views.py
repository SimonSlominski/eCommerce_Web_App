from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import render

from products.models import Product


class SearchProductView(ListView):
    model = Product
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            lookups = Q(name__icontains=query) | Q(description__icontains=query)
            return Product.objects.filter(lookups).distinct()

