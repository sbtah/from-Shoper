import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product
from external.put_products import create_update_for_product_at_shoper
from external.create_url import create_relative_url, create_seo_url_from_id
from external.post_redirects import create_redirect


# CSV PATH TO CODES FOR LANGUAGE TO Update.
CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


def create_update_for_product_for_language(to_lang, make_redirects):
    """
    Send PUT Data from local product model to Shoper's product endpoint by ID.
    Updates data from Local DB to Shoper's DB.
    After successful POST request creates redirect to newly generated SEO URL, if make_redirects is set to True.
    """

    for sku in (f"{row.product_code}" for row in df.itertuples()):
        try:
            product = Product.objects.get(shoper_sku=sku)
            if to_lang == "pl_PL":
                creatation_object = product.prepare_pl_copy_data()
                response = create_update_for_product_at_shoper(
                    shoper_id=product.shoper_id,
                    to_language_code=to_lang,
                    producer_id=product.shoper_producer_id,
                    category_id=product.shoper_category_id,
                    other_price=product.shoper_other_price,
                    code=product.shoper_sku,
                    ean=product.shoper_ean,
                    shoper_vol_weight=product.shoper_vol_weight,
                    stock_price=product.shoper_stock_price,
                    stock_weight=product.shoper_weight,
                    stock_availability_id=product.shoper_availability_id,
                    shoper_delivery_id=product.shoper_delivery_id,
                    translations_name=creatation_object["shoper_translation_name"],
                    translations_active=creatation_object[
                        "shoper_translation_is_active"
                    ],
                    translations_short_description=creatation_object[
                        "shoper_short_description"
                    ],
                    translations_description=creatation_object["shoper_description"],
                )
            if make_redirects == True:
                # Use this part only if function param for making redirects == Y. Otherwise skip.
                if type(response[0]) == "true":
                    create_redirect(
                        from_url=create_relative_url(
                            creatation_object["shoper_permalink"]
                        ),
                        to_url=response[1],
                    )
            else:
                continue
            # TODO:
        except Product.DoesNotExist:
            continue


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def add_arguments(self, parser):

        parser.add_argument(
            "to_language",
            type=str,
            help="Indicates the translation that will be saved",
        )
        parser.add_argument(
            "make_redirects",
            type=bool,
            help="Create redirect from old url to new?",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        to_lang = kwargs["to_language"]
        make_redirects = kwargs["make_redirects"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                ...Update in progress
                """
            )
        )
        print(
            create_update_for_product_for_language(
                to_lang=to_lang, make_redirects=make_redirects
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Update of products finished.
        """
            )
        )
