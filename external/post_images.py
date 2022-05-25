import json
import base64
import time
import logging
import requests
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD


logging.basicConfig(level=logging.INFO)
TOKEN = get_token()


def upload_image_for_product_from_file(product_id, alt_of_img, file_path, language):
    """Upload a new image from FILE for specified product."""

    image = open(file_path, "rb").read()

    data = json.dumps(
        {
            "product_id": f"{product_id}",
            "content": base64.b64encode(image).decode("utf8"),
            "translations": {
                f"{language}": {
                    "name": f"{alt_of_img}",
                },
            },
        }
    )

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res


def upload_image_for_product_from_url(product_id, alt_of_img, source_url, language):
    """Upload a new image from URL for specified product."""

    data = json.dumps(
        {
            "product_id": f"{product_id}",
            "url": f"{source_url}",
            "translations": {
                f"{language}": {
                    "name": f"{alt_of_img}",
                },
            },
        }
    )

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.post(url, headers=headers, data=data)
    res = response.json()
    time.sleep(0.5)

    return res
