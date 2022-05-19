from datetime import datetime
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from products.models import Product
from django.contrib import messages
from django.urls import reverse, reverse_lazy
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


class ProductUpdateFromShoperView(LoginRequiredMixin, generic.DetailView):
    """Update data for Product from API."""

    model = Product
    template_name = "products/product_detail.html"

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        response = get_single_product(product.shoper_id)

        if (
            datetime.strptime(response["updated_shoper"], "%Y-%m-%d %H:%M:%S")
            > product.updated_shoper
        ):
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


def update_product_from_shoper(request, pk):

    if request.method == "GET":
        object = get_single_product(pk)
        print(object)

        return render(request, "products/product_detail.html")
