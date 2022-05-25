import json
import base64
import time
import logging
import requests
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD


logging.basicConfig(level=logging.INFO)
TOKEN = get_token()


# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
        pages = res.get("pages")
    except Exception as e:
        print(e)

    return pages


# https://meowbaby.eu/userdata/public/gfx/4841/MeowBaby® Plastikowe Piłeczki do Suchego Basenu Ø7cm, żółte - 50 szt.jpg
def get_single_gfx_image(id):
    """
    Returns a reponse from product images endpoint.
    https://shop.url/webapi/rest/product-images/<id>
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    image = response.json()

    return image


def get_all_images_for_product(product_id):
    """Get all images for product SKU from SHOPER Api."""

    image_list = []

    for x in range(1, get_number_of_image_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")

        for i in items:
            logging.info(f"Searching for Image")
            time.sleep(0.5)
            if i.get("product_id") == product_id:
                image_list.append(int(i))
                logging.info(f"Image added to list")

    return image_list


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
    time.sleep()

    return res
