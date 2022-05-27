import json
import time
import requests
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD


TOKEN = get_token()


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
    time.sleep(0.5)

    return res


def set_new_seo_url_for_product(
    product_id,
    translation_code,
):
    """
    PUT
    Set new SEO URL for specified product and translation.
    """

    data = json.dumps(
        {
            "translations": {
                f"{translation_code}": {
                    "seo_url": f"",
                }
            },
        }
    )
    url = f"https://{SHOPER_STORE}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.put(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res
