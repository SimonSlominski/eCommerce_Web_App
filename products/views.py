from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()

