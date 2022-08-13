from django.db.models import Q
from products.models import Product
from django.core.management.base import BaseCommand
from external.put_products import set_new_vol_weight_for_product
from external.get_products import get_vol_weight_data_of_product


def query_products_for_language(from_language):

    query = Product.objects.filter(shoper_sku__endswith=from_language)

    return query


def copy_vol_weight_values(from_language, to_language):

    qset = query_products_for_language(from_language)

    with open(f"WEIGHTS.csv", "w") as file:
        file.write(f"product_code;product_id;vol_weight")

    for product in qset:
        # print(product)
        new_lang_prod = Product.objects.get(
            shoper_sku=f"{product.shoper_sku[:-2]}{to_language}"
        )
        print(new_lang_prod)
        # print(
        #     set_new_vol_weight_for_product(
        #         product_id=new_lang_prod.shoper_id, vol_veight=product.shoper_vol_weight
        #     )
        # )
        with open(f"WEIGHTS.csv", "a") as file:
            file.write(f"\n{get_vol_weight_data_of_product(new_lang_prod.shoper_id)}")


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "from_language",
            type=str,
            help="Indicates the translation that will be copied",
        )
        parser.add_argument(
            "to_language",
            type=str,
            help="Indicates the translation that will be saved",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        from_lang = kwargs["from_language"]
        to_lang = kwargs["to_language"]

        self.stdout.write(self.style.SUCCESS(f"Copy data from defined QuerySet"))

        copy_vol_weight_values(
            from_language=from_lang,
            to_language=to_lang,
        )

        self.stdout.write(self.style.SUCCESS(f"Process finished"))
