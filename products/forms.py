from pyexpat import model
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
            "shoper_images",
            "shoper_weight",
            "is_active_shoper",
            "shoper_tags",
            "shoper_price",
            "shoper_gauge_id",
        ]


class PickLanguageToCopyForm(forms.Form):

    from_language = forms.ChoiceField(
        widget=forms.Select(),
        choices=(
            [
                ("pl_PL", "PL"),
                ("de_DE", "DE"),
                ("en_EU", "EU"),
                ("en_GB", "GB"),
                ("fr_FR", "FR"),
                ("en_US", "US"),
            ]
        ),
        initial="1",
        required=True,
    )
    to_language = forms.ChoiceField(
        widget=forms.Select(),
        choices=(
            [
                ("pl_PL", "PL"),
                ("de_DE", "DE"),
                ("en_EU", "EU"),
                ("en_GB", "GB"),
                ("fr_FR", "FR"),
                ("en_US", "US"),
            ]
        ),
        initial="1",
        required=True,
    )
