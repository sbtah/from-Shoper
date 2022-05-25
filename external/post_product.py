import json
import time
import requests
import logging
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD
from external.get_products import get_single_product_data_for_copy
from external.create_url import create_seo_url


TOKEN = get_token()
logging.basicConfig(level=logging.INFO)


# Create a copy of product!
def create_single_product_for_laguage(from_id, from_language_code, to_language_code):
    """Create a copy of product data specified by id and it's language code."""

    product = get_single_product_data_for_copy(from_id, from_language_code)

    data = json.dumps(
        {
            "producer_id": product["producer_id"],
            "category_id": f"{product['category_id']}",
            "other_price": f"{product['other_price']}",
            "code": f"{product['code']}{to_language_code[3:]}",
            "ean": f"{product['ean']}",
            "vol_weight": f"{product['vol_weight']}",
            "stock": {
                "price": f"{product['stock_price']}",
                "weight": f"{product['stock_weight']}",
                # "availability_id": f"{'' if product['stock_availability_id'] == None else product['stock_availability_id']} ",
                "delivery_id": f"{product['stock_delivery_id']}",
                # "gfx_id": f"{'' if product['stock_gfx_id'] == None else product['stock_gfx_id']}",
            },
            "translations": {
                f"{to_language_code}": {
                    "name": f"{product['translations_name']}",
                    "short_description": f"{product['translations_short_description']}",
                    "description": f"{product['translations_description']}",
                    "active": f"{product['translations_active']}",
                    "seo_title": f"",
                    "seo_description": f"",
                    "seo_keywords": f"",
                    "seo_url": create_seo_url(
                        to_language_code, product["translations_name"], from_id
                    ),
                }
            },
        }
    )

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(url, headers=headers, data=data)
    res = response.json()

    return res
