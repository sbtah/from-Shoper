from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from products.models import Product
from django.urls import reverse, reverse_lazy
from products.forms import ProductUpdateFromShoperForm
from products.services import get_single_product


class ProductListView(LoginRequiredMixin, generic.ListView):

    model = Product
    context_object_name = "products"
    paginate_by = 10
    template_name = "products/product_list.html"


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    """DetailView for Product object."""

    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Product object."""

    pass


class ProductUpdateFromShoperView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Product object that pulls data from Shoper API."""

    model = Product
    form_class = ProductUpdateFromShoperForm
    template_name = "products/product_update_from_shoper.html"
    success_url = reverse_lazy("panel:panel")
