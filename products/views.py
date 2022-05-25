from datetime import datetime
from itertools import product
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from products.models import Product
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from products.services import get_single_product
from external.post_product import create_single_product_for_laguage


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


class ProductUpdateFromShoperView(LoginRequiredMixin, generic.DetailView):
    """Update data for Product from API."""

    model = Product
    template_name = "products/product_detail.html"

    def get(self, request, *args, **kwargs):
        """
        Modifed get method that calls get_single_product function from services.py.
        Function returns a dictionary of needed values from API call for ID of product.
        """

        product = self.get_object()
        response = get_single_product(product.shoper_id)

        if datetime.strptime(
            response["updated_shoper"], "%Y-%m-%d %H:%M:%S"
        ) > datetime.strptime(product.updated_shoper, "%Y-%m-%d %H:%M:%S"):
            product.shoper_title_pl = response["shoper_title_pl"]
            product.shoper_title_en = response["shoper_title_en"]
            product.shoper_title_de = response["shoper_title_de"]
            product.shoper_title_fr = response["shoper_title_fr"]
            product.shoper_description_pl = response["shoper_description_pl"]
            product.shoper_description_en = response["shoper_description_en"]
            product.shoper_description_fr = response["shoper_description_fr"]
            product.shoper_description_de = response["shoper_description_de"]
            product.vendor_brand = response["vendor_brand"]
            product.shoper_id = response["shoper_id"]
            product.shoper_ean = response["shoper_ean"]
            product.shoper_sku = response["shoper_sku"]
            product.shoper_weight = response["shoper_weight"]
            product.is_active_shoper = response["is_active_shoper"]
            product.created_shoper = response["created_shoper"]
            product.updated_shoper = response["updated_shoper"]
            product.shoper_price = response["shoper_price"]
            product.shoper_gauge_id = response["shoper_gauge_id"]
            product.is_on_shoper = response["is_on_shoper"]
            product.save()
            messages.success(request, ("Product Updated."))
        else:
            messages.success(request, ("There was nothing to update."))
        return super().get(request, *args, **kwargs)


class CreateLanguageCopyOfProductAtShoper(LoginRequiredMixin, generic.FormView):
    """Update data for Product from API."""

    model = Product
    template_name = "products/product_detail.html"

    # def get(self, request, *args, **kwargs):
    #     print(request)
    #     print(args)
    #     print(kwargs)

    #     product = self.get_object()
    #     print(product)

    #     """
    #     Modifed get method that calls get_single_product function from services.py.
    #     Function returns a dictionary of needed values from API call for ID of product.
    #     """
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # assign the object to the view
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
