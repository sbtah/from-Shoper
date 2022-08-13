import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product


# TODO
# CHANGE FILE !
CSV_PATH = "BESTY.csv"
FILE = pd.read_csv(CSV_PATH, sep=";")


def generate_bestsellers_sku_from_ids(df):

    output_sku = []

    for row in df.itertuples():
        # print(row.id)
        try:
            product = Product.objects.get(shoper_id=row.id)
            output_sku.append(product.shoper_sku)
        except Product.DoesNotExist:
            continue

    return output_sku


def generate_ids_from_sku(df, language):

    for sku in generate_bestsellers_sku_from_ids(df):
        new_sku_for_lang = f"{sku}{language[3:]}"
        # print(new_sku_for_lang)
        try:
            product = Product.objects.get(shoper_sku=new_sku_for_lang)
            print(product.shoper_id)
        except Product.DoesNotExist:
            continue


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def add_arguments(self, parser):

        parser.add_argument(
            "language",
            type=str,
            help="Indicates the translation that will be saved",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        to_lang = kwargs["language"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                ...Update in progress
                """
            )
        )
        # print(generate_bestsellers_sku_for_lang(FILE))
        generate_ids_from_sku(df=FILE, language=to_lang)

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Update of products finished.
        """
            )
        )
