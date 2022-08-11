import json
import time
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.helpers.create_url import create_seo_url


def create_product_at_shoper(
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
    Sends a POST request with Product Data to Shoper's product endpoint.
    Creates a NEW Product and returns JSON response after.
    """
    seo_url = create_seo_url(to_language_code, translations_name, shoper_sku)
    data = json.dumps(
        {
            "producer_id": producer_id,
            "category_id": category_id,
            "other_price": other_price,
            "code": code,
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
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res, seo_url
