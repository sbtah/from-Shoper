import requests
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from products.models import Product
from stocks.models import Stock
from translations.models import ProductTranslation
from external.get_token import SHOPER_STORE, TOKEN
from external.get_products import (
    get_number_of_product_pages,
)


# Get all ID numbers of products from SHOPER Api.
def copy_all_products_from_shoper_api():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    number_of_product_pages = get_number_of_product_pages()
    updated_products = []
    created_products = []
    
    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")

        for i in items:
            """Loops over part of response with all products."""

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
                shoper_category_id = i.get("category_id")
            except AttributeError:
                shoper_category_id = None
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
            # == END of Variables ==
            try:
                product = Product.objects.get(
                    shoper_id=shoper_id,
                )
                if datetime.strptime(
                    updated_shoper, "%Y-%m-%d %H:%M:%S"
                ) > datetime.strptime(product.updated_shoper, "%Y-%m-%d %H:%M:%S"):
                    # Shoper Main Data
                    product.shoper_id = shoper_id
                    product.shoper_type = shoper_type
                    product.shoper_producer_id = shoper_producer_id
                    product.shoper_group_id = shoper_group_id
                    product.shoper_tax_id = shoper_tax_id
                    product.shoper_category_id = shoper_category_id
                    product.shoper_unit_id = shoper_unit_id
                    product.created_shoper = created_shoper
                    product.updated_shoper = updated_shoper
                    product.shoper_other_price = shoper_other_price
                    product.shoper_promo_price = shoper_promo_price
                    product.shoper_sku = shoper_sku
                    product.shoper_ean = shoper_ean
                    product.shoper_pkwiu = shoper_pkwiu
                    product.shoper_is_product_of_day = shoper_is_product_of_day
                    product.shoper_bestseller_tag = shoper_bestseller_tag
                    product.shoper_new_product_tag = shoper_new_product_tag
                    product.shoper_vol_weight = shoper_vol_weight
                    product.shoper_gauge_id = shoper_gauge_id
                    product.shoper_currency_id = shoper_currency_id
                    # Shoper Special Offer.
                    product.shoper_promo_id = shoper_promo_id
                    product.shoper_promo_start = shoper_promo_start
                    product.shoper_promo_ends = shoper_promo_ends
                    product.shoper_discount_value = shoper_discount_value
                    product.save()
                    updated_products.append(product.shoper_id)
                    print(f"UPDATED: {product}")
                else:
                    print(f"No update detected for: {product}")

            except Product.DoesNotExist:
                product = Product.objects.create(
                    shoper_id=shoper_id,
                    shoper_type=shoper_type,
                    shoper_producer_id=shoper_producer_id,
                    shoper_group_id=shoper_group_id,
                    shoper_tax_id=shoper_tax_id,
                    shoper_category_id=shoper_category_id,
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
                    # Shoper Special Offer.
                    shoper_promo_id=shoper_promo_id,
                    shoper_promo_start=shoper_promo_start,
                    shoper_promo_ends=shoper_promo_ends,
                    shoper_discount_value=shoper_discount_value,
                )
                created_products.append(product.shoper_id)
                print(f"CREATED: {product}")
            """
            Loops over part of response with all products.
            """
            print("===STOCK===")
            # Stock data from response.
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
                shoper_stock_calculation_unit_id = i.get("stock").get(
                    "calculation_unit_id"
                )
                shoper_stock_calculation_unit_ratio = i.get("stock").get(
                    "calculation_unit_ratio"
                )
                """===STOCK==="""
                """
                Tries to fetch Product's Stock object from DB and update it.
                Creates new object if fails.
                """
                try:
                    stock = Stock.objects.get(shoper_stock_id=shoper_stock_id)
                    if (
                        (str(stock.shoper_stock_id) != str(shoper_stock_id))
                        or (
                            str(stock.shoper_stock_product_id)
                            != str(shoper_stock_product_id)
                        )
                        or (
                            str(stock.shoper_stock_extended)
                            != str(shoper_stock_extended)
                        )
                        or (str(stock.shoper_stock_price) != str(shoper_stock_price))
                        or (str(stock.shoper_stock_active) != str(shoper_stock_active))
                        or (
                            str(stock.shoper_stock_default) != str(shoper_stock_default)
                        )
                        or (str(stock.shoper_stock_value) != str(shoper_stock_value))
                        or (
                            str(stock.shoper_stock_warn_level)
                            != str(shoper_stock_warn_level)
                        )
                        or (str(stock.shoper_stock_sold) != str(shoper_stock_sold))
                        or (str(stock.shoper_stock_code) != str(shoper_stock_code))
                        or (str(stock.shoper_stock_ean) != str(shoper_stock_ean))
                        or (str(stock.shoper_stock_weight) != str(shoper_stock_weight))
                        or (
                            str(stock.shoper_stock_weight_type)
                            != str(shoper_stock_weight_type)
                        )
                        or (
                            str(stock.shoper_stock_availability_id)
                            != str(shoper_stock_availability_id)
                        )
                        or (
                            str(stock.shoper_stock_delivery_id)
                            != str(shoper_stock_delivery_id)
                        )
                        or (str(stock.shoper_stock_gfx_id) != str(shoper_stock_gfx_id))
                        or (
                            str(stock.shoper_stock_package) != str(shoper_stock_package)
                        )
                        or (
                            str(stock.shoper_stock_price_wholesale)
                            != str(shoper_stock_price_wholesale)
                        )
                        or (
                            str(stock.shoper_stock_price_special)
                            != str(shoper_stock_price_special)
                        )
                        or (
                            str(stock.shoper_stock_calculation_unit_id)
                            != str(shoper_stock_calculation_unit_id)
                        )
                        or (
                            str(stock.shoper_stock_calculation_unit_ratio)
                            != str(shoper_stock_calculation_unit_ratio)
                        )
                    ):
                        stock.shoper_stock_id = shoper_stock_id
                        stock.shoper_stock_product_id = shoper_stock_product_id
                        stock.shoper_stock_extended = shoper_stock_extended
                        stock.shoper_stock_price = shoper_stock_price
                        stock.shoper_stock_active = shoper_stock_active
                        stock.shoper_stock_default = shoper_stock_default
                        stock.shoper_stock_value = shoper_stock_value
                        stock.shoper_stock_warn_level = shoper_stock_warn_level
                        stock.shoper_stock_sold = shoper_stock_sold
                        stock.shoper_stock_code = shoper_stock_code
                        stock.shoper_stock_ean = shoper_stock_ean
                        stock.shoper_stock_weight = shoper_stock_weight
                        stock.shoper_stock_weight_type = shoper_stock_weight_type
                        stock.shoper_stock_availability_id = (
                            shoper_stock_availability_id
                        )
                        stock.shoper_stock_delivery_id = shoper_stock_delivery_id
                        stock.shoper_stock_gfx_id = shoper_stock_gfx_id
                        stock.shoper_stock_package = shoper_stock_package
                        stock.shoper_stock_price_wholesale = (
                            shoper_stock_price_wholesale
                        )
                        stock.shoper_stock_price_special = shoper_stock_price_special
                        stock.shoper_stock_calculation_unit_id = (
                            shoper_stock_calculation_unit_id
                        )
                        stock.shoper_stock_calculation_unit_ratio = (
                            shoper_stock_calculation_unit_ratio
                        )
                        parrent_product = Product.objects.get(
                            shoper_id=stock.shoper_stock_product_id
                        )
                        parrent_product.stock_set.add(stock)
                        stock.save()
                        print(f"Stock: {stock.shoper_stock_id} Updated")
                    else:
                        parrent_product = Product.objects.get(
                            shoper_id=stock.shoper_stock_product_id
                        )
                        parrent_product.stock_set.add(stock)
                        print(f"No updates Stock: {stock.shoper_stock_id}")
                except Stock.DoesNotExist:
                    stock = Stock.objects.create(
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
                    parrent_product = Product.objects.get(
                        shoper_id=stock.shoper_stock_product_id
                    )
                    parrent_product.stock_set.add(stock)
                    print(f"Stock : {stock.shoper_stock_id} Created")
            except TypeError:
                print("Type Error from Stock - no stock values")

            """PRODUCT'S TRANSLATIONS"""
            try:
                for tag in i.get("translations"):

                    """Create Products Translation for each language Tag on current product."""

                    # Get Variables from each of translations that Product currently have.
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
                    description = (
                        i.get("translations").get(f"{locale}").get("description")
                    )
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
                    """
                    Tries to fetch existing Product Translation from DB and update it.
                    Creates new object if fails.
                    """
                    print(locale)
                    print(shoper_translation_id)
                    try:
                        translation = ProductTranslation.objects.get(
                            shoper_translation_id=shoper_translation_id
                        )
                        """
                        Checks is data translation data in DB is not different from response.
                        If there is a difference on one of the fields, model is updated.
                        """
                        if (
                            (str(translation.locale) != str(locale))
                            or (
                                str(translation.shoper_translation_id)
                                != str(shoper_translation_id)
                            )
                            or (
                                str(translation.related_product_id)
                                != str(related_product_id)
                            )
                            or (str(translation.name) != str(name))
                            or (
                                str(translation.short_description)
                                != str(short_description)
                            )
                            or (str(translation.description) != str(description))
                            or (str(translation.active) != str(active))
                            or (str(translation.is_default) != str(is_default))
                            or (str(translation.lang_id) != str(lang_id))
                            or (str(translation.seo_title) != str(seo_title))
                            or (
                                str(translation.seo_description) != str(seo_description)
                            )
                            or (str(translation.seo_keywords) != str(seo_keywords))
                            or (str(translation.seo_url) != str(seo_url))
                            or (str(translation.permalink) != str(permalink))
                            or (str(translation.order) != str(order))
                            or (str(translation.main_page) != str(main_page))
                            or (
                                str(translation.main_page_order) != str(main_page_order)
                            )
                        ):
                            translation.locale = locale
                            translation.shoper_translation_id = shoper_translation_id
                            translation.related_product_id = related_product_id
                            translation.name = name
                            translation.short_description = short_description
                            translation.description = description
                            translation.active = active
                            translation.is_default = is_default
                            translation.lang_id = lang_id
                            translation.seo_title = seo_title
                            translation.seo_description = seo_description
                            translation.seo_keywords = seo_keywords
                            translation.seo_url = seo_url
                            translation.permalink = permalink
                            translation.order = order
                            translation.main_page = main_page
                            translation.description = description
                            translation.main_page_order = main_page_order

                            parrent_product = Product.objects.get(
                                shoper_id=translation.related_product_id
                            )
                            parrent_product.producttranslation_set.add(translation)
                            translation.save()
                            print(
                                f"Translation: {translation.related_product_id} Updated"
                            )
                        else:
                            parrent_product = Product.objects.get(
                                shoper_id=translation.related_product_id
                            )
                            parrent_product.producttranslation_set.add(translation)
                            print(
                                f"No updates for Translation: {translation.related_product_id}"
                            )
                    except ProductTranslation.DoesNotExist:
                        print()
                        translation = ProductTranslation.objects.create(
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
                        parrent_product = Product.objects.get(
                            shoper_id=translation.related_product_id
                        )
                        parrent_product.producttranslation_set.add(translation)
                        print(
                            f"Translation created {translation.shoper_translation_id}"
                        )
            except TypeError:
                print("Type Error from ProductTranslation - No values in loop")
        time.sleep(0.5)
        print(f"Updated Products: {updated_products}")
        print(f"Created Products: {created_products}")
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
