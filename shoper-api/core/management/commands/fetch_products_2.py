from django.core.management.base import BaseCommand
from products.models import Product
from products.builders import update_or_create_product
from stocks.builders import update_or_create_category_stock
from translations.builders import update_or_create_product_translation
from apiclient.products.get_medium import (
    get_all_products_data,
)
from apiclient.products.get_advanced import (
    from_response_product,
    from_response_stock_for_product,
    from_response_translations_for_product,
)
from apiclient.helpers.logging import logging


def fetch_products():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    ### TODO:
    ### TASK : Get all products and translation data from list of IDS.
    ### THIS can be used on list responded from an API or generated from DB.
    ### LONG DISCOVERY TASK : List of IDs is a response from API
    ### SHORTER VALIDATION TASK : List of IDs is a response from local db Products table.
    for data in get_all_products_data():
        product_data = from_response_product(response=data)
        product = update_or_create_product(
            shoper_id=product_data["shoper_id"],
            shoper_type=product_data["shoper_type"],
            shoper_producer_id=product_data["shoper_producer_id"],
            shoper_group_id=product_data["shoper_group_id"],
            shoper_tax_id=product_data["shoper_tax_id"],
            shoper_main_category_id=product_data["shoper_main_category_id"],
            shoper_all_categories_ids=product_data["shoper_all_categories_ids"],
            shoper_unit_id=product_data["shoper_unit_id"],
            created_shoper=product_data["created_shoper"],
            updated_shoper=product_data["updated_shoper"],
            shoper_other_price=product_data["shoper_other_price"],
            shoper_promo_price=product_data["shoper_promo_price"],
            shoper_sku=product_data["shoper_sku"],
            shoper_ean=product_data["shoper_ean"],
            shoper_pkwiu=product_data["shoper_pkwiu"],
            shoper_is_product_of_day=product_data["shoper_is_product_of_day"],
            shoper_bestseller_tag=product_data["shoper_bestseller_tag"],
            shoper_new_product_tag=product_data["shoper_new_product_tag"],
            shoper_vol_weight=product_data["shoper_vol_weight"],
            shoper_gauge_id=product_data["shoper_gauge_id"],
            shoper_currency_id=product_data["shoper_currency_id"],
            shoper_promo_id=product_data["shoper_promo_id"],
            shoper_promo_start=product_data["shoper_promo_start"],
            shoper_promo_ends=product_data["shoper_promo_ends"],
            shoper_discount_value=product_data["shoper_discount_value"],
        )
        logging.info(f"Processed Product: {product}")

        stock_response = from_response_stock_for_product(
            response=product_data["shoper_product_stock"]
        )
        # print(stock_response)
        stock = update_or_create_category_stock(
            shoper_stock_id=stock_response["stock_id"],
            shoper_stock_product_id=stock_response["product_id"],
            shoper_stock_extended=stock_response["extended"],
            shoper_stock_price=stock_response["price"],
            shoper_stock_active=stock_response["active"],
            shoper_stock_default=stock_response["default"],
            shoper_stock_value=stock_response["stock"],
            shoper_stock_warn_level=stock_response["warn_level"],
            shoper_stock_sold=stock_response["sold"],
            shoper_stock_code=stock_response["code"],
            shoper_stock_ean=stock_response["ean"],
            shoper_stock_weight=stock_response["weight"],
            shoper_stock_weight_type=stock_response["weight_type"],
            shoper_stock_availability_id=stock_response["availability_id"],
            shoper_stock_delivery_id=stock_response["delivery_id"],
            shoper_stock_gfx_id=stock_response["gfx_id"],
            shoper_stock_package=stock_response["package"],
            shoper_stock_price_wholesale=stock_response["price_wholesale"],
            shoper_stock_price_special=stock_response["price_special"],
            shoper_stock_calculation_unit_id=stock_response["calculation_unit_id"],
            shoper_stock_calculation_unit_ratio=stock_response[
                "calculation_unit_ratio"
            ],
        )
        logging.info(f"Processed Stock: {stock}")
        translations_data = from_response_translations_for_product(
            response=product_data["shoper_product_translations"]
        )
        for trans in translations_data:
            traslation = update_or_create_product_translation(
                locale=trans["locale"],
                shoper_translation_id=trans["shoper_translation_id"],
                related_product_id=trans["related_product_id"],
                name=trans["name"],
                short_description=trans["short_description"],
                description=trans["description"],
                active=trans["active"],
                is_default=trans["is_default"],
                lang_id=trans["lang_id"],
                seo_title=trans["seo_title"],
                seo_description=trans["seo_description"],
                seo_keywords=trans["seo_keywords"],
                seo_url=trans["seo_url"],
                permalink=trans["permalink"],
                order=trans["order"],
                main_page=trans["main_page"],
                main_page_order=trans["main_page_order"],
            )
            logging.info(f"Processed Translation: {traslation}")


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Product objects count: {Product.objects.all().count()}"
            )
        )
        fetch_products()
        self.stdout.write(self.style.SUCCESS("Database available!"))
