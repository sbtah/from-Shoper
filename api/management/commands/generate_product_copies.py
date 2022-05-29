import pandas as pd
from django.core.management.base import BaseCommand
from products.models import Product
from external.create_url import create_relative_url
from external.post_redirects import create_redirect
from external.post_product import create_copy_of_product_at_shoper
from external.post_images import upload_image_for_product_from_url
from api.management.commands.validate_copy import generate_missing_sku_to_copy


CSV_PATH = "Images.csv"
df = pd.read_csv(CSV_PATH, sep=";")


def create_copies_for_language(from_lang, to_lang, make_redirects, copy_images):
    # I can use filter here
    # query_set = Product.objects.filter(
    #     shoper_sku__in=generate_missing_sku_to_copy(df=df, from_lang=to_lang)
    # )

    # generate_missing_sku_to_copy(df=df, from_lang=to_lang)
    for sku in generate_missing_sku_to_copy(df=df, from_lang=to_lang):
        try:
            product = Product.objects.get(shoper_sku=sku)
            if from_lang == "pl_PL":
                creatation_object = product.prepare_pl_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue

            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
            elif from_lang == "en_GB":
                creatation_object = product.prepare_gb_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue
            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
            elif from_lang == "en_IE":
                creatation_object = product.prepare_eu_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue
            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
            elif from_lang == "fr_FR":
                creatation_object = product.prepare_fr_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue
            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
            elif from_lang == "de_DE":
                creatation_object = product.prepare_de_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue
                # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
            elif from_lang == "en_US":
                creatation_object = product.prepare_us_copy_data()
                response = create_copy_of_product_at_shoper(
                    shoper_sku=product.shoper_sku,
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
                print("RESPONSE FROM CREATE;", response)
                if copy_images == True:
                    # Use this part only if function param for copying images == Y. Otherwise skip.
                    if type(response[0]) == int:
                        images_urls = product.return_images_urls()
                        for url in images_urls:
                            upload_image_for_product_from_url(
                                response[0],
                                creatation_object["shoper_translation_name"],
                                url,
                                to_lang,
                            )
                    else:
                        continue
                if make_redirects == True:
                    # Use this part only if function param for making redirects == Y. Otherwise skip.
                    if type(response[0]) == int:
                        create_redirect(
                            from_url=create_relative_url(
                                creatation_object["shoper_permalink"]
                            ),
                            to_url=response[1],
                        )
                    else:
                        continue
            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.
        except Product.DoesNotExist:
            continue
    return response


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

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
        parser.add_argument(
            "make_redirects",
            type=bool,
            help="Create redirect from old url to new?",
        )
        parser.add_argument(
            "copy_images",
            type=bool,
            help="Copy images upon cration of product?",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""
        from_lang = kwargs["from_language"]
        to_lang = kwargs["to_language"]
        make_redirects = kwargs["make_redirects"]
        copy_images = kwargs["copy_images"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                ...Copy in progress
                """
            )
        )
        print(
            create_copies_for_language(from_lang, to_lang, make_redirects, copy_images)
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Copy of products finished.
        """
            )
        )
