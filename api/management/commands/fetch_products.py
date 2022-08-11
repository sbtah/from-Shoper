from django.core.management.base import BaseCommand
from products.models import Product
from products.builders import update_or_create_product
from stocks.builders import update_or_create_category_stock
from translations.builders import update_or_create_product_translation
from external.get_products import get_all_products_data


def fetch_products():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    for i in get_all_products_data():
        # Shoper Main Data
        try:
            shoper_id = i.get("product_id")
        except AttributeError:
            shoper_id = ""
        try:
            shoper_type = i.get("type")
        except AttributeError:
            shoper_type = None
        try:
            shoper_producer_id = i.get("producer_id")
        except AttributeError:
            shoper_producer_id = None
        try:
            shoper_group_id = i.get("group_id")
        except AttributeError:
            shoper_group_id = None
        try:
            shoper_tax_id = i.get("tax_id")
        except AttributeError:
            shoper_tax_id = None
        try:
            shoper_main_category_id = i.get("category_id")
        except AttributeError:
            shoper_main_category_id = None
        try:
            shoper_all_categories_ids = i.get("categories")
        except AttributeError:
            shoper_all_categories_ids = []
        try:
            shoper_unit_id = i.get("unit_id")
        except AttributeError:
            shoper_unit_id = None
        try:
            created_shoper = i.get("add_date")
        except AttributeError:
            created_shoper = ""
        try:
            updated_shoper = i.get("edit_date")
        except AttributeError:
            updated_shoper = ""
        try:
            shoper_other_price = i.get("other_price")
        except AttributeError:
            shoper_other_price = ""
        try:
            shoper_promo_price = i.get("promo_price")
        except AttributeError:
            shoper_promo_price = ""
        try:
            shoper_sku = i.get("code")
        except AttributeError:
            shoper_sku = ""
        try:
            shoper_ean = i.get("ean")
        except AttributeError:
            shoper_ean = ""
        try:
            shoper_pkwiu = i.get("pkwiu")
        except AttributeError:
            shoper_pkwiu = ""
        try:
            shoper_is_product_of_day = i.get("is_product_of_day")
        except AttributeError:
            shoper_is_product_of_day = ""
        try:
            shoper_bestseller_tag = i.get("bestseller")
        except AttributeError:
            shoper_bestseller_tag = ""
        try:
            shoper_new_product_tag = i.get("newproduct")
        except AttributeError:
            shoper_new_product_tag = ""
        try:
            shoper_vol_weight = i.get("vol_weight")
        except AttributeError:
            shoper_vol_weight = ""
        try:
            shoper_gauge_id = i.get("gauge_id")
        except AttributeError:
            shoper_gauge_id = None
        try:
            shoper_currency_id = i.get("currency_id")
        except AttributeError:
            shoper_currency_id = None
        # Shoper Special Offer.
        try:
            shoper_promo_id = i.get("special_offer").get("promo_id")
        except AttributeError:
            shoper_promo_id = None
        try:
            shoper_promo_start = i.get("special_offer").get("date_from")
        except AttributeError:
            shoper_promo_start = ""
        try:
            shoper_promo_ends = i.get("special_offer").get("date_to")
        except AttributeError:
            shoper_promo_ends = ""
        try:
            shoper_discount_value = i.get("special_offer").get("discount")
        except AttributeError:
            shoper_discount_value = ""

        update_or_create_product(
            shoper_id=shoper_id,
            shoper_type=shoper_type,
            shoper_producer_id=shoper_producer_id,
            shoper_group_id=shoper_group_id,
            shoper_tax_id=shoper_tax_id,
            shoper_main_category_id=shoper_main_category_id,
            shoper_all_categories_ids=shoper_all_categories_ids,
            shoper_unit_id=shoper_unit_id,
            created_shoper=created_shoper,
            updated_shoper=updated_shoper,
            shoper_other_price=shoper_other_price,
            shoper_promo_price=shoper_promo_price,
            shoper_sku=shoper_sku,
            shoper_ean=shoper_ean,
            shoper_pkwiu=shoper_pkwiu,
            shoper_is_product_of_day=shoper_is_product_of_day,
            shoper_bestseller_tag=shoper_bestseller_tag,
            shoper_new_product_tag=shoper_new_product_tag,
            shoper_vol_weight=shoper_vol_weight,
            shoper_gauge_id=shoper_gauge_id,
            shoper_currency_id=shoper_currency_id,
            shoper_promo_id=shoper_promo_id,
            shoper_promo_start=shoper_promo_start,
            shoper_promo_ends=shoper_promo_ends,
            shoper_discount_value=shoper_discount_value,
        )
        try:
            shoper_stock_id = i.get("stock").get("stock_id")
            shoper_stock_product_id = i.get("stock").get("product_id")
            shoper_stock_extended = i.get("stock").get("extended")
            shoper_stock_price = i.get("stock").get("price")
            shoper_stock_active = i.get("stock").get("active")
            shoper_stock_default = i.get("stock").get("default")
            shoper_stock_value = i.get("stock").get("stock")
            shoper_stock_warn_level = i.get("stock").get("warn_level")
            shoper_stock_sold = i.get("stock").get("sold")
            shoper_stock_code = i.get("stock").get("code")
            shoper_stock_ean = i.get("stock").get("ean")
            shoper_stock_weight = i.get("stock").get("weight")
            shoper_stock_weight_type = i.get("stock").get("weight_type")
            shoper_stock_availability_id = i.get("stock").get("availability_id")
            shoper_stock_delivery_id = i.get("stock").get("delivery_id")
            shoper_stock_gfx_id = i.get("stock").get("gfx_id")
            shoper_stock_package = i.get("stock").get("package")
            shoper_stock_price_wholesale = i.get("stock").get("price_wholesale")
            shoper_stock_price_special = i.get("stock").get("price_special")
            shoper_stock_calculation_unit_id = i.get("stock").get("calculation_unit_id")
            shoper_stock_calculation_unit_ratio = i.get("stock").get(
                "calculation_unit_ratio"
            )
            update_or_create_category_stock(
                shoper_stock_id=shoper_stock_id,
                shoper_stock_product_id=shoper_stock_product_id,
                shoper_stock_extended=shoper_stock_extended,
                shoper_stock_price=shoper_stock_price,
                shoper_stock_active=shoper_stock_active,
                shoper_stock_default=shoper_stock_default,
                shoper_stock_value=shoper_stock_value,
                shoper_stock_warn_level=shoper_stock_warn_level,
                shoper_stock_sold=shoper_stock_sold,
                shoper_stock_code=shoper_stock_code,
                shoper_stock_ean=shoper_stock_ean,
                shoper_stock_weight=shoper_stock_weight,
                shoper_stock_weight_type=shoper_stock_weight_type,
                shoper_stock_availability_id=shoper_stock_availability_id,
                shoper_stock_delivery_id=shoper_stock_delivery_id,
                shoper_stock_gfx_id=shoper_stock_gfx_id,
                shoper_stock_package=shoper_stock_package,
                shoper_stock_price_wholesale=shoper_stock_price_wholesale,
                shoper_stock_price_special=shoper_stock_price_special,
                shoper_stock_calculation_unit_id=shoper_stock_calculation_unit_id,
                shoper_stock_calculation_unit_ratio=shoper_stock_calculation_unit_ratio,
            )
        except TypeError:
            print("Type Error from Stock - no stock values")
        try:
            for tag in i.get("translations"):
                locale = tag
                shoper_translation_id = (
                    i.get("translations").get(f"{locale}").get("translation_id")
                )
                related_product_id = (
                    i.get("translations").get(f"{locale}").get("product_id")
                )
                name = i.get("translations").get(f"{locale}").get("name")
                short_description = (
                    i.get("translations").get(f"{locale}").get("short_description")
                )
                description = i.get("translations").get(f"{locale}").get("description")
                active = i.get("translations").get(f"{locale}").get("active")
                is_default = i.get("translations").get(f"{locale}").get("isdefault")
                lang_id = i.get("translations").get(f"{locale}").get("lang_id")
                seo_title = i.get("translations").get(f"{locale}").get("seo_title")
                seo_description = (
                    i.get("translations").get(f"{locale}").get("seo_description")
                )
                seo_keywords = (
                    i.get("translations").get(f"{locale}").get("seo_keywords")
                )
                seo_url = i.get("translations").get(f"{locale}").get("seo_url")
                permalink = i.get("translations").get(f"{locale}").get("permalink")
                order = i.get("translations").get(f"{locale}").get("order")
                main_page = i.get("translations").get(f"{locale}").get("main_page")
                main_page_order = (
                    i.get("translations").get(f"{locale}").get("main_page_order")
                )
                update_or_create_product_translation(
                    locale=locale,
                    shoper_translation_id=shoper_translation_id,
                    related_product_id=related_product_id,
                    name=name,
                    short_description=short_description,
                    description=description,
                    active=active,
                    is_default=is_default,
                    lang_id=lang_id,
                    seo_title=seo_title,
                    seo_description=seo_description,
                    seo_keywords=seo_keywords,
                    seo_url=seo_url,
                    permalink=permalink,
                    order=order,
                    main_page=main_page,
                    main_page_order=main_page_order,
                )
        except TypeError:
            print("Type Error from ProductTranslation - No values in loop")
    return


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
