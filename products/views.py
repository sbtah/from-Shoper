from datetime import datetime
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from products.services import get_single_product
from products.forms import PickLanguageToCopyForm
from external.get_products import get_single_product
from products.services import create_copy_of_product_at_shoper


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
        print(product)
        # Call get_single_product function from services.py
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


class CreateLanguageCopyOfProductAtShoper(
    LoginRequiredMixin, FormMixin, generic.DetailView
):
    """Update data for Product from API."""

    model = Product
    form_class = PickLanguageToCopyForm
    template_name = "products/product_create_copy_at_shoper.html"

    def get_success_url(self):
        view_name = "products:product-detail"
        product = self.get_object()
        return reverse(view_name, kwargs={"pk": product.id})

    def get(self, request, *args, **kwargs):

        # print(get_single_product(102))

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """

        from_product = Product.objects.get(pk=kwargs.get("pk"))

        form = self.get_form()
        if form.is_valid():
            from_language = form.cleaned_data["from_language"]
            to_language = form.cleaned_data["to_language"]
            if from_language == "pl_PL":
                creatation_object = from_product.prepare_pl_copy_data()
                print(creatation_object)
                response = create_copy_of_product_at_shoper(
                    to_language_code=to_language,
                    producer_id=from_product.producer_id,
                    category_id=from_product.category_id,
                    other_price=from_product.other_price,
                    code=from_product.shoper_sku,
                    ean=from_product.shoper_ean,
                    shoper_vol_weight=from_product.shoper_vol_weigh,
                    stock_price=from_product.shoper_stock_price,
                    stock_weight=from_product.shoper_weight,
                    stock_availability_id=from_product.shoper_availability_id,
                    shoper_delivery_id=from_product.shoper_delivery_id,
                    translations_name=creatation_object["shoper_translation_name"],
                    translations_active=creatation_object[
                        "shoper_translation_is_active"
                    ],
                    translations_short_description=creatation_object[
                        "translations_short_description"
                    ],
                    translations_description=creatation_object[
                        "translations_description"
                    ],
                    seo_description=creatation_object["seo_description"],
                )
                # call a function from services.py that sends post req with creation object at Shoper store.
            elif from_language == "en_GB":
                creatation_object = from_product.prepare_gb_copy_data()
                print(creatation_object)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)
