import json
import time
import requests
from helpers.get_token import SHOPER_DOMAIN, TOKEN
from helpers.create_url import create_seo_url, create_relative_url


def deacivate_translation_for_product(product_id, translation_code):
    """
    PUT
    Turns off specified translation for specified product.
    """

    data = json.dumps(
        {
            "translations": {
                f"{translation_code}": {
                    "name": "",
                    "active": 0,
                }
            },
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res


def set_new_title_for_products_translation(product_id, translation_code, name):
    """
    PUT
    Sets new title for translation for specified product.
    """

    data = json.dumps(
        {
            "translations": {
                f"{translation_code}": {
                    "name": f"{name}",
                }
            },
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res


def set_new_vol_weight_for_product(product_id, vol_veight):
    """
    PUT
    Sets new vol_weight for specified product.
    """

    data = json.dumps(
        {
            "vol_weight": vol_veight,
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res


def set_new_seo_url_for_products_translation(
    product_id, to_language, product_name, product_sku
):
    """
    PUT
    Set new SEO URL for specified product and translation.
    """

    data = json.dumps(
        {
            "translations": {
                f"{to_language}": {
                    "seo_url": f"{create_seo_url(language_code=to_language, product_name=product_name, shoper_sku=product_sku)}",
                }
            },
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res


def create_update_for_product_at_shoper(
    shoper_id,
    shoper_sku,
    to_language_code,
    producer_id,
    category_id,
    other_price,
    code,
    ean,
    shoper_vol_weight,
    stock_price,
    stock_weight,
    stock_availability_id,
    shoper_delivery_id,
    translations_name,
    translations_active,
    translations_short_description,
    translations_description,
):
    """
    USED IN DJANGO.
    Sends a PUT request with Product Data to Shoper's product endpoint.
    Updates existing product.
    """
    seo_url = create_seo_url(to_language_code, translations_name, shoper_sku)
    data = json.dumps(
        {
            "producer_id": producer_id,
            "category_id": category_id,
            "other_price": other_price,
            "code": f"{code}",
            "ean": ean,
            "vol_weight": shoper_vol_weight,
            "stock": {
                "price": stock_price,
                "weight": stock_weight,
                "availability_id": stock_availability_id,
                "delivery_id": shoper_delivery_id,
            },
            "translations": {
                f"{to_language_code}": {
                    "name": translations_name,
                    "short_description": translations_short_description,
                    "description": translations_description,
                    "active": translations_active,
                    "seo_title": "",
                    "seo_description": "",
                    "seo_keywords": "",
                    "seo_url": seo_url,
                }
            },
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{shoper_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res, seo_url
