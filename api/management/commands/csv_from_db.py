import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product
from external.get_products import (
    get_list_of_all_shoper_product_sku,
    get_list_of_all_shoper_product_ids,
)


# CSV PATH TO CODES FOR LANGUAGE TO Update.
CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


# def generate_product_data(lang_code, file_name, to_csv):

#     with open(f"{file_name}.csv", "r") as file:
#         file.write(f"Shoper ID;SKU;NAME;LINK;SEO-LINK")

#     for sku in (f"{row.product_code}" for row in df.itertuples()):
#         try:
#             product = Product.objects.get(shoper_sku=sku)
#             with open(f"{file_name}.csv", "a") as file:
#                 file.write(
#                     f"\n{product.shoper_id};{product.shoper_sku};{product.current_link};{product.seo_link}"
#                 )

#         except Product.DoesNotExist:
#             continue


def start():
    return get_list_of_all_shoper_product_ids()


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "on_language_tag",
    #         type=str,
    #         help="Indicates the translation that turned of on products.",
    #     )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Generate categories data.
                """
            )
        )

        print(start())
        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Process finished
                """
            )
        )
