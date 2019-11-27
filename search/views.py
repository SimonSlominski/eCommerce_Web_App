from django.views.generic import ListView
from django.shortcuts import render

from products.models import Product


class SearchProductView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.filter(title_icontains=query)
        return Product.objects.none()
    # def get_context_data(self, *args, **kwargs):
    #     context = super(SearchProductView, self).get_context_data(*args, **kwargs)
    #     return context
