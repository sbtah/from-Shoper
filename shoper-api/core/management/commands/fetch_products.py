from products.models import Product
from django.core.management.base import BaseCommand
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


def fetch_products_v2():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    products_data = get_all_products_data()
    for prod in products_data:

        logging.info("=" * 78)
        logging.info(f'PROCESSING: Product id: {prod["product_id"]}')
        product_data = from_response_product(
            response=prod,
        )
        # print(product_data["shoper_id"])
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
        stock_response = from_response_stock_for_product(
            response=product_data["shoper_product_stock"]
        )
        stock = update_or_create_category_stock(
            shoper_stock_id=stock_response["shoper_stock_id"],
            shoper_stock_product_id=stock_response["shoper_stock_product_id"],
            shoper_stock_extended=stock_response["shoper_stock_extended"],
            shoper_stock_price=stock_response["shoper_stock_price"],
            shoper_stock_active=stock_response["shoper_stock_active"],
            shoper_stock_default=stock_response["shoper_stock_default"],
            shoper_stock_value=stock_response["shoper_stock_value"],
            shoper_stock_warn_level=stock_response["shoper_stock_warn_level"],
            shoper_stock_sold=stock_response["shoper_stock_sold"],
            shoper_stock_code=stock_response["shoper_stock_code"],
            shoper_stock_ean=stock_response["shoper_stock_ean"],
            shoper_stock_weight=stock_response["shoper_stock_weight"],
            shoper_stock_weight_type=stock_response["shoper_stock_weight_type"],
            shoper_stock_availability_id=stock_response["shoper_stock_availability_id"],
            shoper_stock_delivery_id=stock_response["shoper_stock_delivery_id"],
            shoper_stock_gfx_id=stock_response["shoper_stock_gfx_id"],
            shoper_stock_package=stock_response["shoper_stock_package"],
            shoper_stock_price_wholesale=stock_response["shoper_stock_price_wholesale"],
            shoper_stock_price_special=stock_response["shoper_stock_price_special"],
            shoper_stock_calculation_unit_id=stock_response[
                "shoper_stock_calculation_unit_id"
            ],
            shoper_stock_calculation_unit_ratio=stock_response[
                "shoper_stock_calculation_unit_ratio"
            ],
        )
        # print(stock_response)
        translations = from_response_translations_for_product(
            response=product_data["shoper_product_translations"],
        )
        for trans in translations:
            # print(trans["locale"])
            translation = update_or_create_product_translation(
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


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Product objects count: {Product.objects.all().count()}"
            )
        )
        fetch_products_v2()
        self.stdout.write(self.style.SUCCESS("Database available!"))
