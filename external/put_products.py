import json
import time
import requests
import logging
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD
from external.get_products import get_single_product_data_for_copy


TOKEN = get_token()
logging.basicConfig(level=logging.INFO)


def deacivate_translation_for_product(product_id, translation_code):
    """
    PUT
    Turns off specified translation for specified produt.
    """

    data = json.dumps(
        {
            "translations": {
                f"{translation_code}": {
                    "active": 0,
                }
            },
        }
    )
    url = f"https://{SHOPER_STORE}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()

    return res
