import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product


CSV_PATH = "FR-NAMES.csv"


FILE = pd.read_csv(CSV_PATH, sep=";", encoding="ISO-8859-1", engine="python")


def load_names_for_language(data_frame, to_language):
    """Load names from CSV file and store them im local field realated to picked translation"""

    for row in data_frame.itertuples():
        sku = row.product_code[0:-2]
        # print(sku)
        try:
            product = Product.objects.get(shoper_sku=sku)
            if to_language == "pl_Pl":
                product.shoper_title_pl = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_pl}")

            elif to_language == "en_GB":
                product.shoper_title_gb = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_gb}")

            elif to_language == "en_IE":
                product.shoper_title_eu = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_eu}")

            elif to_language == "fr_FR":
                product.shoper_title_fr = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_fr}")

            elif to_language == "de_DE":
                product.shoper_title_de = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_fr}")

            elif to_language == "en_US":
                product.shoper_title_us = row.name
                product.save()
                print(f"{product.shoper_id}: {product.shoper_title_us}")

        except Product.DoesNotExist as e:
            continue


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "to_language",
            type=str,
            help="Indicates the target translation in which new name will be stored.",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        to_lang = kwargs["to_language"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                ...Copy in progress
                """
            )
        )
        load_names_for_language(
            FILE,
            to_lang,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Copy of products finished.
        """
            )
        )
