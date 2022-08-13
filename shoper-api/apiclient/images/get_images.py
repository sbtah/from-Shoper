import json
import base64
import time
import logging
import requests
from helpers.get_token import SHOPER_DOMAIN, TOKEN


# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
        pages = res.get("pages")
    except Exception as e:
        print(e)

    return pages


def get_single_gfx_image(id):
    """
    Returns a reponse from product images endpoint.
    https://shop.url/webapi/rest/product-images/<id>
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    image = response.json()

    return image


def get_all_images_data():
    """Get all Product Images for all pages from Shoper Api."""

    number_of_images_pages = get_number_of_image_pages()

    for x in range(1, number_of_images_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        time.sleep(0.5)
        res = response.json()
        items = res.get("list")

        for i in items:
            yield i


def get_all_images_for_product(product_id):
    """Get all images for product SKU from SHOPER Api."""

    image_list = []

    for x in range(1, get_number_of_image_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
