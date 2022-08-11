from datetime import datetime
from re import U
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from products.builders import update_or_create_product
from products.forms import PickLanguageToCopyForm
from external.get_products import get_single_product
from external.post_redirects import create_redirect
from external.create_url import create_relative_url
from images.models import Image


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

    def get_context_data(self, **kwargs):
        """Get data about Images, Stocks and Translations related to this object."""

        context = super().get_context_data(**kwargs)

        product = kwargs.get("object")
        context["related_images"] = product.image_set.all()
        context["related_stock"] = product.stock_set.get(
            shoper_stock_product_id=product.shoper_id
        )
        context["related_translations"] = product.producttranslation_set.all()

        return context


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Product object."""

    pass


class ProductUpdateFromShoperView(LoginRequiredMixin, generic.DetailView):
    """Update data for Product and related Images, Stocks and Translations from Shoper's API."""

    model = Product
    template_name = "products/product_detail.html"

    def get(self, request, *args, **kwargs):
        """
        Modifed get method that calls get_single_product function from services.py.
        Function returns a dictionary of needed values from API call for ID of product.
        """

        product = self.get_object()
        # Call get_single_product function from external app.
        response = get_single_product(product.shoper_id)

        if datetime.strptime(
            response["edit_date"], "%Y-%m-%d %H:%M:%S"
        ) > datetime.strptime(product.updated_shoper, "%Y-%m-%d %H:%M:%S"):
            product.product.shoper_type = response["type"]
            product.shoper_producer_id = response["producer_id"]
            product.shoper_group_id = response["group_id"]
            product.shoper_tax_id = response["tax_id"]
            product.shoper_main_category_id = response["category_id"]
            product.shoper_all_categories_ids = response["categories"]
            product.shoper_unit_id = response["unit_id"]
            product.created_shoper = response["add_date"]
            product.updated_shoper = response["edit_date"]
            product.shoper_other_price = response["other_price"]
            product.shoper_promo_price = response["promo_price"]
            product.shoper_sku = response["code"]
            product.shoper_ean = response["ean"]
            product.shoper_pkwiu = response["pkwiu"]
            product.shoper_is_product_of_day = response["is_product_of_day"]
            product.shoper_bestseller_tag = response["bestseller"]
            product.shoper_new_product_tag = response["newproduct"]
            product.shoper_vol_weight = response["vol_weight"]
            product.shoper_gauge_id = response["gauge_id"]
            product.shoper_currency_id = response["currency_id"]
            product.shoper_promo_id = response.get("special_offer").get("promo_id")
            product.shoper_promo_start = response.get("special_offer").get("date_from")
            product.shoper_promo_ends = response.get("special_offer").get("date_to")
            product.shoper_discount_value = response.get("special_offer").get("discount")
            for x in response["translations"]:
                print(x)
            # Todo add stock, translations , images and categories
            # product.save()
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
        # TODO
        # Implement a 3rd Form picker: Create Redirect from original? Y | N
        # Implement a 4th Form picker: Copy pictures from original? Y | N
        from_product = Product.objects.get(pk=kwargs.get("pk"))

        form = self.get_form()
        if form.is_valid():
            from_language = form.cleaned_data["from_language"]
            to_language = form.cleaned_data["to_language"]
            if from_language == "pl_PL":
                # Calls a Product object method that returns needed values for creation of copy for language
                creatation_object = from_product.prepare_pl_copy_data()
                # Calls a helper function that sends a POST request to SHOPER Api and creates a copy of Product.
                response = create_copy_of_product_at_shoper(
                    shoper_sku=from_product.shoper_sku,
                    to_language_code=to_language,
                    producer_id=from_product.shoper_producer_id,
                    category_id=from_product.shoper_category_id,
                    other_price=from_product.shoper_other_price,
                    code=from_product.shoper_sku,
                    ean=from_product.shoper_ean,
                    shoper_vol_weight=from_product.shoper_vol_weight,
                    stock_price=from_product.shoper_stock_price,
                    stock_weight=from_product.shoper_weight,
                    stock_availability_id=from_product.shoper_availability_id,
                    shoper_delivery_id=from_product.shoper_delivery_id,
                    translations_name=creatation_object["shoper_translation_name"],
                    translations_active=creatation_object[
                        "shoper_translation_is_active"
                    ],
                    translations_short_description=creatation_object[
                        "shoper_short_description"
                    ],
                    translations_description=creatation_object["shoper_description"],
                )
                # TODO
                # Use this part only if form value for making redirects == Y. Otherwise skip.
                if type(response[0]) == int:
                    create_redirect(
                        from_url=create_relative_url(
                            creatation_object["shoper_permalink"]
                        ),
                        to_url=response[1],
                    )
                else:
                    pass
                # TODO
                #
                # TODO:
                # Work with this response to create a local instance of new created product at Shoper.
            elif from_language == "en_GB":
                creatation_object = from_product.prepare_gb_copy_data()
                # Calls a Product object method that returns needed values for creation of copy for language
                print(creatation_object)
                # Calls a helper function that sends a POST request to SHOPER Api and creates a copy of Product.
                response = create_copy_of_product_at_shoper(
                    shoper_sku=from_product.shoper_sku,
                    to_language_code=to_language,
                    producer_id=from_product.shoper_producer_id,
                    category_id=from_product.shoper_category_id,
                    other_price=from_product.shoper_other_price,
                    code=from_product.shoper_sku,
                    ean=from_product.shoper_ean,
                    shoper_vol_weight=from_product.shoper_vol_weight,
                    stock_price=from_product.shoper_stock_price,
                    stock_weight=from_product.shoper_weight,
                    stock_availability_id=from_product.shoper_availability_id,
                    shoper_delivery_id=from_product.shoper_delivery_id,
                    translations_name=creatation_object["shoper_translation_name"],
                    translations_active=creatation_object[
                        "shoper_translation_is_active"
                    ],
                    translations_short_description=creatation_object[
                        "shoper_short_description"
                    ],
                    translations_description=creatation_object["shoper_description"],
                )
                print(response)
                # TODO:
                # Work with this response to create a local instance of new created product at Shoper.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
