import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product
from external.put_products import deacivate_translation_for_product


# CSV PATH TO CODES FOR LANGUAGE TO Update.
CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


def turn_of_translation(on_language_tag):

    for sku in (f"{row.product_code}" for row in df.itertuples()):

        try:
            product = Product.objects.get(shoper_sku=sku)
            print(product)
            deacivate_translation_for_product(
                product_id=product.shoper_id, translation_code=on_language_tag
            )
        except Product.DoesNotExist:
            continue


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "on_language_tag",
            type=str,
            help="Indicates the translation that turned of on products.",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        on_language_tag = kwargs["on_language_tag"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Turning off translation(s)
                """
            )
        )
        turn_of_translation(on_language_tag)

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Process finished
                """
            )
        )
