import requests
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from products.models import Product
from translations.models import ProductTranslation
from external.get_token import SHOPER_STORE, TOKEN
from external.get_products import get_number_of_product_pages


# Get all ID numbers of products from SHOPER Api.
def copy_all_products_from_shoper_api():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    number_of_product_pages = get_number_of_product_pages()

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            shoper_product_id = i.get("product_id")
            print(shoper_product_id)
            try:
                for tag in i.get("translations"):

                    translation = ProductTranslation.objects.update_or_create(
                        locale=tag,
                        shoper_translation_id=i.get("translations")
                        .get(tag)
                        .get("translation_id"),
                        related_product_id=i.get("translations")
                        .get(tag)
                        .get("product_id"),
                        name=i.get("translations").get(tag).get("name"),
                        short_description=i.get("translations")
                        .get(tag)
                        .get("short_description"),
                        description=i.get("translations").get(tag).get("description"),
                        active=i.get("translations").get(tag).get("active"),
                        is_default=i.get("translations").get(tag).get("isdefault"),
                        lang_id=i.get("translations").get(tag).get("lang_id"),
                        seo_title=i.get("translations").get(tag).get("seo_title"),
                        seo_description=i.get("translations")
                        .get(tag)
                        .get("seo_description"),
                        seo_keywords=i.get("translations").get(tag).get("seo_keywords"),
                        seo_url=i.get("translations").get(tag).get("seo_url"),
                        permalink=i.get("translations").get(tag).get("permalink"),
                        order=i.get("translations").get(tag).get("order"),
                        main_page=i.get("translations").get(tag).get("main_page"),
                        main_page_order=i.get("translations")
                        .get(tag)
                        .get("main_page_order"),
                    )
                    print(f"Translation:{translation[0]}")
                    print(f"Created:{translation[1]}")
            except TypeError:
                continue

            # Shoper Main Data
            try:
                shoper_id = i.get("product_id")
            except AttributeError:
                shoper_id = ""
            try:
                shoper_ean = i.get("ean")
            except AttributeError:
                shoper_ean = ""
            try:
                shoper_sku = i.get("code")
            except AttributeError:
                shoper_sku = ""
            try:
                shoper_vol_weight = i.get("vol_weight")
            except AttributeError:
                shoper_vol_weight = ""
            try:
                is_active_shoper = i.get("stock").get("active")  # Test it!
            except AttributeError:
                is_active_shoper = ""
            try:
                created_shoper = i.get("add_date")
            except AttributeError:
                created_shoper = ""
            try:
                updated_shoper = i.get("edit_date")
            except AttributeError:
                updated_shoper = ""
            try:
                shoper_stock_price = i.get("stock").get("price")
            except AttributeError:
                shoper_stock_price = ""
            try:
                shoper_producer_id = i.get("producer_id")
            except AttributeError:
                shoper_producer_id = None
            try:
                shoper_category_id = i.get("category_id")
            except AttributeError:
                shoper_category_id = None
            try:
                shoper_delivery_id = i.get("stock").get("delivery_id")
            except AttributeError:
                shoper_delivery_id = None
            try:
                shoper_other_price = i.get("other_price")
            except AttributeError:
                shoper_other_price = None
            try:
                shoper_gauge_id = i.get("gauge_id")
            except AttributeError:
                shoper_gauge_id = None
            try:
                shoper_bestseller_tag = i.get("bestseller")
            except AttributeError:
                shoper_bestseller_tag = ""
            try:
                shoper_new_product_tag = i.get("newproduct")
            except AttributeError:
                shoper_new_product_tag = ""
            try:
                shoper_unit_id = i.get("unit_id")
            except AttributeError:
                shoper_unit_id = None
            try:
                shoper_currency_id = i.get("currency_id")
            except AttributeError:
                shoper_currency_id = None
            try:
                shoper_weight = i.get("stock").get("weight")
            except AttributeError:
                shoper_weight = ""
            try:
                shoper_availability_id = i.get("shoper_availability_id")
            except AttributeError:
                shoper_availability_id = None
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
            # PL SEO DATA
            try:
                shoper_title_pl = i.get("translations").get("pl_PL").get("name")
            except AttributeError:
                shoper_title_pl = ""
            try:
                shoper_translation_is_active_pl = (
                    i.get("translations").get("pl_PL").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_pl = ""
            try:
                shoper_short_description_pl = (
                    i.get("translations").get("pl_PL").get("short_description")
                )
            except AttributeError:
                shoper_short_description_pl = ""
            try:
                shoper_description_pl = (
                    i.get("translations").get("pl_PL").get("description")
                )
            except AttributeError:
                shoper_description_pl = ""
            try:
                shoper_seo_title_pl = (
                    i.get("translations").get("pl_PL").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_pl = ""
            try:
                shoper_meta_desc_pl = (
                    i.get("translations").get("pl_PL").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_pl = ""
            try:
                shoper_permalink_pl = (
                    i.get("translations").get("pl_PL").get("permalink")
                )
            except AttributeError:
                shoper_permalink_pl = ""
            try:
                shoper_seo_url_pl = i.get("translations").get("pl_PL").get("seo_url")
            except AttributeError:
                shoper_seo_url_pl = ""
            # GB SEO DATA
            try:
                shoper_title_gb = i.get("translations").get("en_GB").get("name")
            except AttributeError:
                shoper_title_gb = ""
            try:
                shoper_translation_is_active_gb = (
                    i.get("translations").get("en_GB").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_gb = ""
            try:
                shoper_short_description_gb = (
                    i.get("translations").get("en_GB").get("short_description")
                )
            except AttributeError:
                shoper_short_description_gb = ""
            try:
                shoper_description_gb = (
                    i.get("translations").get("en_GB").get("description")
                )
            except AttributeError:
                shoper_description_gb = ""
            try:
                shoper_seo_title_gb = (
                    i.get("translations").get("en_GB").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_gb = ""
            try:
                shoper_meta_desc_gb = (
                    i.get("translations").get("en_GB").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_gb = ""
            try:
                shoper_permalink_gb = (
                    i.get("translations").get("en_GB").get("permalink")
                )
            except AttributeError:
                shoper_permalink_gb = ""
            try:
                shoper_seo_url_gb = i.get("translations").get("en_GB").get("seo_url")
            except AttributeError:
                shoper_seo_url_gb = ""
            # EU SEO DATA
            try:
                shoper_title_eu = i.get("translations").get("en_EU").get("name")
            except AttributeError:
                shoper_title_eu = ""
            try:
                shoper_translation_is_active_eu = (
                    i.get("translations").get("en_IE").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_eu = ""
            try:
                shoper_short_description_eu = (
                    i.get("translations").get("en_IE").get("short_description")
                )
            except AttributeError:
                shoper_short_description_eu = ""
            try:
                shoper_description_eu = (
                    i.get("translations").get("en_IE").get("description")
                )
            except AttributeError:
                shoper_description_eu = ""
            try:
                shoper_seo_title_eu = (
                    i.get("translations").get("en_IE").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_eu = ""
            try:
                shoper_meta_desc_eu = (
                    i.get("translations").get("en_IE").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_eu = ""
            try:
                shoper_permalink_eu = (
                    i.get("translations").get("en_IE").get("permalink")
                )
            except AttributeError:
                shoper_permalink_eu = ""
            try:
                shoper_seo_url_eu = i.get("translations").get("en_IE").get("seo_url")
            except AttributeError:
                shoper_seo_url_eu = ""
            # FR SEO DATA
            try:
                shoper_title_fr = i.get("translations").get("fr_FR").get("name")
            except AttributeError:
                shoper_title_fr = ""
            try:
                shoper_translation_is_active_fr = (
                    i.get("translations").get("fr_FR").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_fr = ""
            try:
                shoper_short_description_fr = (
                    i.get("translations").get("fr_FR").get("short_description")
                )
            except AttributeError:
                shoper_short_description_fr = ""
            try:
                shoper_description_fr = (
                    i.get("translations").get("fr_FR").get("description")
                )
            except AttributeError:
                shoper_description_fr = ""
            try:
                shoper_seo_title_fr = (
                    i.get("translations").get("fr_FR").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_fr = ""
            try:
                shoper_meta_desc_fr = (
                    i.get("translations").get("fr_FR").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_fr = ""
            try:
                shoper_permalink_fr = (
                    i.get("translations").get("fr_FR").get("permalink")
                )
            except AttributeError:
                shoper_permalink_fr = ""
            try:
                shoper_seo_url_fr = i.get("translations").get("fr_FR").get("seo_url")
            except AttributeError:
                shoper_seo_url_fr = ""
            # DE SEO DATA
            try:
                shoper_title_de = i.get("translations").get("de_DE").get("name")
            except AttributeError:
                shoper_title_de = ""
            try:
                shoper_translation_is_active_de = (
                    i.get("translations").get("de_DE").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_de = ""

            try:
                shoper_short_description_de = (
                    i.get("translations").get("de_DE").get("short_description")
                )
            except AttributeError:
                shoper_short_description_de = ""

            try:
                shoper_description_de = (
                    i.get("translations").get("de_DE").get("description")
                )
            except AttributeError:
                shoper_description_de = ""
            try:
                shoper_seo_title_de = (
                    i.get("translations").get("de_DE").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_de = ""
            try:
                shoper_meta_desc_de = (
                    i.get("translations").get("de_DE").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_de = ""
            try:
                shoper_permalink_de = (
                    i.get("translations").get("de_DE").get("permalink")
                )
            except AttributeError:
                shoper_permalink_de = ""
            try:
                shoper_seo_url_de = i.get("translations").get("de_DE").get("seo_url")
            except AttributeError:
                shoper_seo_url_de = ""
            # US SEO DATA
            try:
                shoper_title_us = i.get("translations").get("en_US").get("name")
            except AttributeError:
                shoper_title_us = ""
            try:
                shoper_translation_is_active_us = (
                    i.get("translations").get("en_US").get("active")
                )
            except AttributeError:
                shoper_translation_is_active_us = ""

            try:
                shoper_short_description_us = (
                    i.get("translations").get("en_US").get("short_description")
                )
            except AttributeError:
                shoper_short_description_us = ""

            try:
                shoper_description_us = (
                    i.get("translations").get("en_US").get("description")
                )
            except AttributeError:
                shoper_description_us = ""
            try:
                shoper_seo_title_us = (
                    i.get("translations").get("en_US").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_us = ""
            try:
                shoper_meta_desc_us = (
                    i.get("translations").get("en_US").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_us = ""
            try:
                shoper_permalink_us = (
                    i.get("translations").get("en_US").get("permalink")
                )
            except AttributeError:
                shoper_permalink_us = ""
            try:
                shoper_seo_url_us = i.get("translations").get("en_US").get("seo_url")
            except AttributeError:
                shoper_seo_url_us = ""
            # Local Data
            try:
                vendor_brand = SHOPER_STORE[0:-3].capitalize()
            except AttributeError:
                vendor_brand = ""
            # == END of Variables ==
            try:
                product = Product.objects.get(
                    shoper_id=shoper_id,
                )
                print(f"DEBUG val:shoper_id from Product: {product.shoper_id}")
                print(f"DEBUG val:shoper_id from GET : {shoper_id}")
                if datetime.strptime(
                    updated_shoper, "%Y-%m-%d %H:%M:%S"
                ) > datetime.strptime(product.updated_shoper, "%Y-%m-%d %H:%M:%S"):
                    # Shoper Main Data
                    product.shoper_id = shoper_id
                    product.shoper_ean = shoper_ean
                    product.shoper_sku = shoper_sku
                    product.shoper_vol_weight = shoper_vol_weight
                    product.is_active_shoper = is_active_shoper
                    product.created_shoper = created_shoper
                    product.updated_shoper = updated_shoper
                    product.shoper_stock_price = shoper_stock_price
                    product.shoper_producer_id = shoper_producer_id
                    product.shoper_category_id = shoper_category_id
                    product.shoper_delivery_id = shoper_delivery_id
                    product.shoper_other_price = shoper_other_price
                    product.shoper_gauge_id = shoper_gauge_id
                    product.shoper_bestseller_tag = shoper_bestseller_tag
                    product.shoper_new_product_tag = shoper_new_product_tag
                    product.shoper_unit_id = shoper_unit_id
                    product.shoper_currency_id = shoper_currency_id
                    product.shoper_weight = shoper_weight
                    product.shoper_availability_id = shoper_availability_id
                    # Shoper Special Offer.
                    product.shoper_promo_id = shoper_promo_id
                    product.shoper_promo_start = shoper_promo_start
                    product.shoper_promo_ends = shoper_promo_ends
                    product.shoper_discount_value = shoper_discount_value
                    # PL SEO DATA
                    product.shoper_title_pl = shoper_title_pl
                    product.shoper_translation_is_active_pl = (
                        shoper_translation_is_active_pl
                    )
                    product.shoper_short_description_pl = shoper_short_description_pl
                    product.shoper_description_pl = shoper_description_pl
                    product.shoper_seo_title_pl = shoper_seo_title_pl
                    product.shoper_meta_desc_pl = shoper_meta_desc_pl
                    product.shoper_permalink_pl = shoper_permalink_pl
                    product.shoper_seo_url_pl = shoper_seo_url_pl
                    # GB SEO DATA
                    product.shoper_title_gb = shoper_title_gb
                    product.shoper_translation_is_active_gb = (
                        shoper_translation_is_active_gb
                    )
                    product.shoper_short_description_gb = shoper_short_description_gb
                    product.shoper_description_gb = shoper_description_gb
                    product.shoper_seo_title_gb = shoper_seo_title_gb
                    product.shoper_meta_desc_gb = shoper_meta_desc_gb
                    product.shoper_permalink_gb = shoper_permalink_gb
                    product.shoper_seo_url_gb = shoper_seo_url_gb
                    # EU SEO DATA
                    product.shoper_title_eu = shoper_title_eu
                    product.shoper_translation_is_active_eu = (
                        shoper_translation_is_active_eu
                    )
                    product.shoper_short_description_eu = shoper_short_description_eu
                    product.shoper_description_eu = shoper_description_eu
                    product.shoper_seo_title_eu = shoper_seo_title_eu
                    product.shoper_meta_desc_eu = shoper_meta_desc_eu
                    product.shoper_permalink_eu = shoper_permalink_eu
                    product.shoper_seo_url_eu = shoper_seo_url_eu
                    # FR SEO DATA
                    product.shoper_title_fr = shoper_title_fr
                    product.shoper_translation_is_active_fr = (
                        shoper_translation_is_active_fr
                    )
                    product.shoper_short_description_fr = shoper_short_description_fr
                    product.shoper_description_fr = shoper_description_fr
                    product.shoper_seo_title_fr = shoper_seo_title_fr
                    product.shoper_meta_desc_fr = shoper_meta_desc_fr
                    product.shoper_permalink_fr = shoper_permalink_fr
                    product.shoper_seo_url_fr = shoper_seo_url_fr
                    # DE SEO DATA
                    product.shoper_title_de = shoper_title_de
                    product.shoper_translation_is_active_de = (
                        shoper_translation_is_active_de
                    )
                    product.shoper_short_description_de = shoper_short_description_de
                    product.shoper_description_de = shoper_description_de
                    product.shoper_seo_title_de = shoper_seo_title_de
                    product.shoper_meta_desc_de = shoper_meta_desc_de
                    product.shoper_permalink_de = shoper_permalink_de
                    product.shoper_seo_url_de = shoper_seo_url_de
                    # US SEO DATA
                    product.shoper_title_us = shoper_title_us
                    product.shoper_translation_is_active_us = (
                        shoper_translation_is_active_us
                    )
                    product.shoper_short_description_us = shoper_short_description_us
                    product.shoper_description_us = shoper_description_us
                    product.shoper_seo_title_us = shoper_seo_title_us
                    product.shoper_meta_desc_us = shoper_meta_desc_us
                    product.shoper_permalink_us = shoper_permalink_us
                    product.shoper_seo_url_us = shoper_seo_url_us

                    # Local Data
                    product.vendor_brand = vendor_brand
                    product.save()
                    print(f"UPDATED: {product}")
                else:
                    print(f"No update detected for: {product}")
                    continue
            except Product.DoesNotExist:
                Product.objects.create(
                    # Shoper Main Data
                    shoper_id=shoper_id,
                    shoper_ean=shoper_ean,
                    shoper_sku=shoper_sku,
                    shoper_vol_weight=shoper_vol_weight,
                    is_active_shoper=is_active_shoper,
                    created_shoper=created_shoper,
                    updated_shoper=updated_shoper,
                    shoper_stock_price=shoper_stock_price,
                    shoper_producer_id=shoper_producer_id,
                    shoper_category_id=shoper_category_id,
                    shoper_delivery_id=shoper_delivery_id,
                    shoper_other_price=shoper_other_price,
                    shoper_gauge_id=shoper_gauge_id,
                    shoper_bestseller_tag=shoper_bestseller_tag,
                    shoper_new_product_tag=shoper_new_product_tag,
                    shoper_unit_id=shoper_unit_id,
                    shoper_currency_id=shoper_currency_id,
                    shoper_weight=shoper_weight,
                    shoper_availability_id=shoper_availability_id,
                    # Shoper Special Offer.
                    shoper_promo_id=shoper_promo_id,
                    shoper_promo_start=shoper_promo_start,
                    shoper_promo_ends=shoper_promo_ends,
                    shoper_discount_value=shoper_discount_value,
                    # PL SEO DATA
                    shoper_title_pl=shoper_title_pl,
                    shoper_translation_is_active_pl=shoper_translation_is_active_pl,
                    shoper_short_description_pl=shoper_short_description_pl,
                    shoper_description_pl=shoper_description_pl,
                    shoper_seo_title_pl=shoper_seo_title_pl,
                    shoper_meta_desc_pl=shoper_meta_desc_pl,
                    shoper_permalink_pl=shoper_permalink_pl,
                    shoper_seo_url_pl=shoper_seo_url_pl,
                    # GB SEO DATA
                    shoper_title_gb=shoper_title_gb,
                    shoper_translation_is_active_gb=shoper_translation_is_active_gb,
                    shoper_short_description_gb=shoper_short_description_gb,
                    shoper_description_gb=shoper_description_gb,
                    shoper_seo_title_gb=shoper_seo_title_gb,
                    shoper_meta_desc_gb=shoper_meta_desc_gb,
                    shoper_permalink_gb=shoper_permalink_gb,
                    shoper_seo_url_gb=shoper_seo_url_gb,
                    # EU SEO DATA
                    shoper_title_eu=shoper_title_eu,
                    shoper_translation_is_active_eu=shoper_translation_is_active_eu,
                    shoper_short_description_eu=shoper_short_description_eu,
                    shoper_description_eu=shoper_description_eu,
                    shoper_seo_title_eu=shoper_seo_title_eu,
                    shoper_meta_desc_eu=shoper_meta_desc_eu,
                    shoper_permalink_eu=shoper_permalink_eu,
                    shoper_seo_url_eu=shoper_seo_url_eu,
                    # FR SEO DATA
                    shoper_title_fr=shoper_title_fr,
                    shoper_translation_is_active_fr=shoper_translation_is_active_fr,
                    shoper_short_description_fr=shoper_short_description_fr,
                    shoper_description_fr=shoper_description_fr,
                    shoper_seo_title_fr=shoper_seo_title_fr,
                    shoper_meta_desc_fr=shoper_meta_desc_fr,
                    shoper_permalink_fr=shoper_permalink_fr,
                    shoper_seo_url_fr=shoper_seo_url_fr,
                    # DE SEO DATA
                    shoper_title_de=shoper_title_de,
                    shoper_translation_is_active_de=shoper_translation_is_active_de,
                    shoper_short_description_de=shoper_short_description_de,
                    shoper_description_de=shoper_description_de,
                    shoper_seo_title_de=shoper_seo_title_de,
                    shoper_meta_desc_de=shoper_meta_desc_de,
                    shoper_permalink_de=shoper_permalink_de,
                    shoper_seo_url_de=shoper_seo_url_de,
                    # US SEO DATA
                    shoper_title_us=shoper_title_us,
                    shoper_translation_is_active_us=shoper_translation_is_active_us,
                    shoper_short_description_us=shoper_short_description_us,
                    shoper_description_us=shoper_description_us,
                    shoper_seo_title_us=shoper_seo_title_us,
                    shoper_meta_desc_us=shoper_meta_desc_us,
                    shoper_permalink_us=shoper_permalink_us,
                    shoper_seo_url_us=shoper_seo_url_us,
                    # Local
                    vendor_brand=vendor_brand,
                )
                print(f"CREATED: {Product}")
            time.sleep(1)
    return


def clear_data():
    """Use only to clear data for Products from DB. For test use only."""
    Product.objects.all().delete()


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Product objects count: {Product.objects.all().count()}"
            )
        )
        copy_all_products_from_shoper_api()
        self.stdout.write(self.style.SUCCESS("Database available!"))
