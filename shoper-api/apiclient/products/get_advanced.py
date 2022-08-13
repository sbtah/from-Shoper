import time
from token import AT
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.helpers.logging import logging
from apiclient.products.get_basic import get_number_of_product_pages


def get_all_shoper_product_ids_for_lang(lang_code):
    """
    Custom search function.
    Works only if language code is in your SKU codes.
    Yield all Product IDs in your Shoper store for language tag in your SKU.
    It's slow, since it loops all products and yields only those that match...
    """

    number_of_product_pages = get_number_of_product_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        try:
            response = requests.get(url, headers=headers, params=data)
            time.sleep(0.5)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            logging.error("Connection was timed out.")
            return None
        except requests.exceptions.ConnectionError:
            logging.error("Connection Error.")
            return None
        except requests.exceptions.HTTPError:
            logging.error("HTTPError was raised.")
            return None
        except Exception as e:
            logging.error(f"(get_all_products_data) Exception: {e}")
        else:
            res = response.json()
            products = res.get("list")
            try:
                for product in products:
                    if lang_code in product.get("code"):
                        yield product.get("product_id")
                        logging.info(f"ID: {product.get('product_id')} - Found")
                    else:
                        logging.info(f"Language tag not found in SKU, passing...")
            except Exception as e:
                logging.error(f"Some nasty exception : {e}")
                break


def get_all_shoper_product_skus_for_lang(lang_code):
    """
    Custom search function.
    Works only if language code is in your SKU codes.
    Yield all Product SKU codes in your Shoper store for language tag in your SKU.
    It's slow, since it loops all products and yields only those that match...
    """

    number_of_product_pages = get_number_of_product_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        try:
            response = requests.get(url, headers=headers, params=data)
            time.sleep(0.5)
            response.raise_for_status()
        except requests.exceptions.Timeout:
            logging.error("Connection was timed out.")
            return None
        except requests.exceptions.ConnectionError:
            logging.error("Connection Error.")
            return None
        except requests.exceptions.HTTPError:
            logging.error("HTTPError was raised.")
            return None
        except Exception as e:
            logging.error(f"(get_all_products_data) Exception: {e}")
        else:
            res = response.json()
            products = res.get("list")
            try:
                for product in products:
                    if lang_code in product.get("code"):
                        yield product.get("code")
                        logging.info(f"SKU: {product.get('code')} - Found")
                    else:
                        logging.info(f"Language tag not found in SKU, passing...")
            except Exception as e:
                logging.error(f"Some nasty exception : {e}")
                break


def get_single_product_data(product_id):
    """
    Sends GET request to Shoper's product API endpoint that returns data for single product.
    Properly selects and cleans data from reponse and stores it the variables.
    Variables are used in dictionary that is returned by this function.
    Used for generating copy data for duplication of product via Shoper API.
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.3)
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(get_single_product_data) Exception: {e}")
    else:
        i = response.json()
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

        try:
            shoper_product_translations = i.get("translations")
        except AttributeError:
            shoper_product_translations = ""

        try:
            shoper_product_stock = i.get("stock")
        except AttributeError:
            shoper_product_stock = ""

        return {
            "shoper_id": shoper_id,
            "shoper_type": shoper_type,
            "shoper_producer_id": shoper_producer_id,
            "shoper_group_id": shoper_group_id,
            "shoper_tax_id": shoper_tax_id,
            "shoper_main_category_id": shoper_main_category_id,
            "shoper_all_categories_ids": shoper_all_categories_ids,
            "shoper_unit_id": shoper_unit_id,
            "created_shoper": created_shoper,
            "updated_shoper": updated_shoper,
            "shoper_other_price": shoper_other_price,
            "shoper_promo_price": shoper_promo_price,
            "shoper_sku": shoper_sku,
            "shoper_ean": shoper_ean,
            "shoper_pkwiu": shoper_pkwiu,
            "shoper_is_product_of_day": shoper_is_product_of_day,
            "shoper_bestseller_tag": shoper_bestseller_tag,
            "shoper_new_product_tag": shoper_new_product_tag,
            "shoper_vol_weight": shoper_vol_weight,
            "shoper_gauge_id": shoper_gauge_id,
            "shoper_currency_id": shoper_currency_id,
            "shoper_promo_id": shoper_promo_id,
            "shoper_promo_start": shoper_promo_start,
            "shoper_promo_ends": shoper_promo_ends,
            "shoper_discount_value": shoper_discount_value,
            "shoper_product_translations": shoper_product_translations,
            "shoper_product_stock": shoper_product_stock,
        }


def from_response_product(response):
    """
    Parses product data from Shoper Api.
    Stores data in proper variables and returns dictionary of needed data for product.
    """

    try:
        shoper_id = response.get("product_id")
    except AttributeError:
        shoper_id = ""
    try:
        shoper_type = response.get("type")
    except AttributeError:
        shoper_type = None
    try:
        shoper_producer_id = response.get("producer_id")
    except AttributeError:
        shoper_producer_id = None
    try:
        shoper_group_id = response.get("group_id")
    except AttributeError:
        shoper_group_id = None
    try:
        shoper_tax_id = response.get("tax_id")
    except AttributeError:
        shoper_tax_id = None
    try:
        shoper_main_category_id = response.get("category_id")
    except AttributeError:
        shoper_main_category_id = None
    try:
        shoper_all_categories_ids = response.get("categories")
    except AttributeError:
        shoper_all_categories_ids = []
    try:
        shoper_unit_id = response.get("unit_id")
    except AttributeError:
        shoper_unit_id = None
    try:
        created_shoper = response.get("add_date")
    except AttributeError:
        created_shoper = ""
    try:
        updated_shoper = response.get("edit_date")
    except AttributeError:
        updated_shoper = ""
    try:
        shoper_other_price = response.get("other_price")
    except AttributeError:
        shoper_other_price = ""
    try:
        shoper_promo_price = response.get("promo_price")
    except AttributeError:
        shoper_promo_price = ""
    try:
        shoper_sku = response.get("code")
    except AttributeError:
        shoper_sku = ""
    try:
        shoper_ean = response.get("ean")
    except AttributeError:
        shoper_ean = ""
    try:
        shoper_pkwiu = response.get("pkwiu")
    except AttributeError:
        shoper_pkwiu = ""
    try:
        shoper_is_product_of_day = response.get("is_product_of_day")
    except AttributeError:
        shoper_is_product_of_day = ""
    try:
        shoper_bestseller_tag = response.get("bestseller")
    except AttributeError:
        shoper_bestseller_tag = ""
    try:
        shoper_new_product_tag = response.get("newproduct")
    except AttributeError:
        shoper_new_product_tag = ""
    try:
        shoper_vol_weight = response.get("vol_weight")
    except AttributeError:
        shoper_vol_weight = ""
    try:
        shoper_gauge_id = response.get("gauge_id")
    except AttributeError:
        shoper_gauge_id = None
    try:
        shoper_currency_id = response.get("currency_id")
    except AttributeError:
        shoper_currency_id = None
    # Shoper Special Offer.
    try:
        shoper_promo_id = response.get("special_offer").get("promo_id")
    except AttributeError:
        shoper_promo_id = None
    try:
        shoper_promo_start = response.get("special_offer").get("date_from")
    except AttributeError:
        shoper_promo_start = ""
    try:
        shoper_promo_ends = response.get("special_offer").get("date_to")
    except AttributeError:
        shoper_promo_ends = ""
    try:
        shoper_discount_value = response.get("special_offer").get("discount")
    except AttributeError:
        shoper_discount_value = ""

    try:
        shoper_product_translations = response.get("translations")
    except AttributeError:
        shoper_product_translations = ""

    try:
        shoper_product_stock = response.get("stock")
    except AttributeError:
        shoper_product_stock = ""

    return {
        "shoper_id": shoper_id,
        "shoper_type": shoper_type,
        "shoper_producer_id": shoper_producer_id,
        "shoper_group_id": shoper_group_id,
        "shoper_tax_id": shoper_tax_id,
        "shoper_main_category_id": shoper_main_category_id,
        "shoper_all_categories_ids": shoper_all_categories_ids,
        "shoper_unit_id": shoper_unit_id,
        "created_shoper": created_shoper,
        "updated_shoper": updated_shoper,
        "shoper_other_price": shoper_other_price,
        "shoper_promo_price": shoper_promo_price,
        "shoper_sku": shoper_sku,
        "shoper_ean": shoper_ean,
        "shoper_pkwiu": shoper_pkwiu,
        "shoper_is_product_of_day": shoper_is_product_of_day,
        "shoper_bestseller_tag": shoper_bestseller_tag,
        "shoper_new_product_tag": shoper_new_product_tag,
        "shoper_vol_weight": shoper_vol_weight,
        "shoper_gauge_id": shoper_gauge_id,
        "shoper_currency_id": shoper_currency_id,
        "shoper_promo_id": shoper_promo_id,
        "shoper_promo_start": shoper_promo_start,
        "shoper_promo_ends": shoper_promo_ends,
        "shoper_discount_value": shoper_discount_value,
        "shoper_product_translations": shoper_product_translations,
        "shoper_product_stock": shoper_product_stock,
    }


def from_response_translations_for_product(response):
    """"""
    try:
        for translation in response.items():
            tag = translation[0]
            shoper_translation_id = translation[1].get("translation_id")
            related_product_id = translation[1].get("product_id")
            name = translation[1].get("name")
            short_description = translation[1].get("short_description")
            description = translation[1].get("description")
            active = translation[1].get("active")
            is_default = translation[1].get("lang_id")
            lang_id = translation[1].get("lang_id")
            seo_title = translation[1].get("seo_title")
            seo_description = translation[1].get("seo_description")
            seo_keywords = translation[1].get("seo_keywords")
            seo_url = translation[1].get("seo_url")
            permalink = translation[1].get("permalink")
            order = translation[1].get("order")
            main_page = translation[1].get("main_page")
            main_page_order = translation[1].get("main_page_order")
            yield {
                "locale": tag,
                "shoper_translation_id": shoper_translation_id,
                "related_product_id": related_product_id,
                "name": name,
                "short_description": short_description,
                "description": description,
                "active": active,
                "is_default": is_default,
                "lang_id": lang_id,
                "seo_title": seo_title,
                "seo_description": seo_description,
                "seo_keywords": seo_keywords,
                "seo_url": seo_url,
                "permalink": permalink,
                "order": order,
                "main_page": main_page,
                "main_page_order": main_page_order,
            }
    except Exception as e:
        logging.error(f"Error while getting response: {e}")


def from_response_stock_for_product(response):
    """"""

    try:
        shoper_stock_id = response.get("stock_id")
        shoper_stock_product_id = response.get("product_id")
        shoper_stock_extended = response.get("extended")
        shoper_stock_price = response.get("price")
        shoper_stock_active = response.get("active")
        shoper_stock_default = response.get("default")
        shoper_stock_value = response.get("stock")
        shoper_stock_warn_level = response.get("warn_level")
        shoper_stock_sold = response.get("sold")
        shoper_stock_code = response.get("code")
        shoper_stock_ean = response.get("ean")
        shoper_stock_weight = response.get("weight")
        shoper_stock_weight_type = response.get("weight_type")
        shoper_stock_availability_id = response.get("availability_id")
        shoper_stock_delivery_id = response.get("delivery_id")
        shoper_stock_gfx_id = response.get("gfx_id")
        shoper_stock_package = response.get("package")
        shoper_stock_price_wholesale = response.get("price_wholesale")
        shoper_stock_price_special = response.get("price_special")
        shoper_stock_calculation_unit_id = response.get("calculation_unit_id")
        shoper_stock_calculation_unit_ratio = response.get("calculation_unit_ratio")
    except Exception as e:
        logging.error(f"Error while getting response: {e}")
    else:
        return {
            "shoper_stock_id": shoper_stock_id,
            "shoper_stock_product_id": shoper_stock_product_id,
            "shoper_stock_extended": shoper_stock_extended,
            "shoper_stock_price": shoper_stock_price,
            "shoper_stock_active": shoper_stock_active,
            "shoper_stock_default": shoper_stock_default,
            "shoper_stock_value": shoper_stock_value,
            "shoper_stock_warn_level": shoper_stock_warn_level,
            "shoper_stock_sold": shoper_stock_sold,
            "shoper_stock_code": shoper_stock_code,
            "shoper_stock_ean": shoper_stock_ean,
            "shoper_stock_weight": shoper_stock_weight,
            "shoper_stock_weight_type": shoper_stock_weight_type,
            "shoper_stock_availability_id": shoper_stock_availability_id,
            "shoper_stock_delivery_id": shoper_stock_delivery_id,
            "shoper_stock_gfx_id": shoper_stock_gfx_id,
            "shoper_stock_package": shoper_stock_package,
            "shoper_stock_price_wholesale": shoper_stock_price_wholesale,
            "shoper_stock_price_special": shoper_stock_price_special,
            "shoper_stock_calculation_unit_id": shoper_stock_calculation_unit_id,
            "shoper_stock_calculation_unit_ratio": shoper_stock_calculation_unit_ratio,
        }
