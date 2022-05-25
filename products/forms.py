from django import forms
from products.models import Product
from products.services import get_single_product


class ProductUpdateFromShoperForm(forms.ModelForm):
    """Form for updating Product object from Shoper API."""

    class Meta:
        model = Product
        fields = [
            "shoper_title_pl",
            "shoper_title_en",
            "shoper_title_fr",
            "shoper_title_de",
            "shoper_description_pl",
            "shoper_description_en",
            "shoper_description_de",
            "vendor_brand",
            "shoper_ean",
            "shoper_sku",
            "images",
            "shoper_weight",
            "is_active_shoper",
            "shoper_tags",
            "shoper_price",
            "shoper_gauge_id",
            "is_on_shoper",
        ]


class PickLanguagetoCopyForm(forms.Form):
    """"""
