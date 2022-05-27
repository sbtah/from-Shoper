from external.token import get_token
from external.token import SHOPER_STORE
from django.core.management.base import BaseCommand
from products.models import Product
from external.create_url import create_relative_url
from external.post_redirects import create_redirect
from external.post_product import create_copy_of_product_at_shoper


TOKEN = get_token()


def create_copies_for_language(from_lang, to_lang, make_redirects, copy_images):
    # I can use filter here
    query_set = Product.objects.filter(
        shoper_id=1448
    )  ### CHANGE TO GET for single ID before testing!

    # TODO
    # Implement a 3rd Form picker Create Redirect from original? Y | N
    # Implement a 4th Form picker: Copy pictures from original? Y | N
    for product in query_set:

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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            # TODO
            # Use this part only if function param for making redirects == Y. Otherwise skip.
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
            # TODO
            # Use this part only if function param for making redirects == Y. Otherwise skip.
            # Create another PUT request to id reponded back by create_copy_of_product_at_shoper function.
            # Loop over Image links list that will be generated on model
            # Create new images from links for called product ID.
            # TODO:
            # Work with this response to create a local instance of new created product at Shoper.

        elif from_lang == "en_GB":
            creatation_object = product.prepare_gb_copy_data()
            response = create_copy_of_product_at_shoper(
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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
        elif from_lang == "en_IE":
            creatation_object = product.prepare_eu_copy_data()
            response = create_copy_of_product_at_shoper(
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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
        elif from_lang == "fr_FR":
            creatation_object = product.prepare_fr_copy_data()
            response = create_copy_of_product_at_shoper(
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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
        elif from_lang == "de_DE":
            creatation_object = product.prepare_de_copy_data()
            response = create_copy_of_product_at_shoper(
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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
        elif from_lang == "en_US":
            creatation_object = product.prepare_us_copy_data()
            response = create_copy_of_product_at_shoper(
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
                translations_active=creatation_object["shoper_translation_is_active"],
                translations_short_description=creatation_object[
                    "shoper_short_description"
                ],
                translations_description=creatation_object["shoper_description"],
            )
            if type(response[0]) == int:
                create_redirect(
                    from_url=create_relative_url(creatation_object["shoper_permalink"]),
                    to_url=response[1],
                )
            else:
                pass
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
            help="Indicates the translation that will be copied",
        )
        parser.add_argument(
            "make_redirects",
            type=str,
            help="Indicates the translation that will be copied",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""
        from_lang = kwargs["from_language"]
        to_lang = kwargs["to_language"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                ...Copy in progress
                """
            )
        )
        print(create_copies_for_language(from_lang, to_lang))

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Copy of products finished.
        """
            )
        )
