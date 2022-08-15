import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product
from external.put_products import set_new_title_for_products_translation


# TODO
# Rework to generate queryset
# CSV PATH TO CODES FOR LANGUAGE TO Update.
CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


def send_new_name(on_language_tag):

    query_set = Product.objects.filter(shoper_sku__endswith=f"{on_language_tag[3:]}")

    # for sku in (f"{row.product_code}{on_language_tag[3:]}" for row in df.itertuples()):
    for object in query_set:
        try:
            # product = Product.objects.get(shoper_sku=sku)
            if on_language_tag == "pl_PL":
                product_seo_data = object.prepare_pl_copy_data()
                if product_seo_data["shoper_seo_url"] != "":
                    print(product_seo_data["shoper_seo_url"])
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

            elif on_language_tag == "en_GB":
                product_seo_data = object.prepare_gb_copy_data()
                if product_seo_data["shoper_seo_url"] != "":
                    print(product_seo_data["shoper_seo_url"])
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

            elif on_language_tag == "en_IE":
                product_seo_data = object.prepare_eu_copy_data()
                if product_seo_data["shoper_seo_url"] != "":
                    print(product_seo_data["shoper_seo_url"])
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

            elif on_language_tag == "fr_FR":

                product_seo_data = object.prepare_fr_copy_data()

                if product_seo_data["shoper_seo_url"] != "":
                    print(f"Setting {on_language_tag[3:]} title @{object.shoper_id}")
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

            elif on_language_tag == "de_DE":
                product_seo_data = object.prepare_de_copy_data()
                if product_seo_data["shoper_seo_url"] != "":
                    print(product_seo_data["shoper_seo_url"])
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

            elif on_language_tag == "en_US":
                product_seo_data = object.prepare_us_copy_data()
                if product_seo_data["shoper_seo_url"] != "":
                    print(product_seo_data["shoper_seo_url"])
                    set_new_title_for_products_translation(
                        product_id=object.shoper_id,
                        translation_code=on_language_tag,
                        name=product_seo_data["shoper_translation_name"],
                    )
                else:
                    print(f"Product:{object.shoper_id} no permalink -  skipping")
                    continue

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
        send_new_name(on_language_tag)

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Process finished
                """
            )
        )
