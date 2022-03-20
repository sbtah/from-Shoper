import requests
import time
import os
import json
from dotenv import load_dotenv


# Get private data fron .env variable
load_dotenv()
SHOPER_LOGIN = os.environ.get("SHOPER_LOGIN")
SHOPER_PASSWORD = os.environ.get("SHOPER_PASSWORD")
SHOPER_STORE = os.environ.get("SHOPER_STORE")


# Get a token by login to your store.
def get_token():
    """Generates fresh token from SHOPER API."""

    url_login = f"https://{SHOPER_STORE}/webapi/rest/auth"
    response = requests.post(url_login, auth=(SHOPER_LOGIN, SHOPER_PASSWORD))
    access_token = response.json().get("access_token")
    return access_token


# Get instance of TOKEN.
TOKEN = get_token()


def get_all_products():
    """Return a paginated response with all products and number of pages."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


def get_product_images(id):
    """Returns a reponse from product images endpoint.
    https://shop.url/webapi/rest/product-images/<id>
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


# Get number of pages for for product list API.
def get_number_of_pages():
    """Get number of all pages from your api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


# Get all ID numbers of products from your DB.
def get_all_ids():
    """Get all product ids from SHOPER Api and push"""
    test_list = []

    for x in range(1, get_number_of_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            test_list.append(int(i.get("product_id")))
            print(f"{i.get('product_id')} - Added to list.")
            time.sleep(0.5)

    return test_list


def get_product_data_for_shopify(list):
    """Get product data necessary for creation of product in Shopify"""

    for x in list:
        print(f"Pobieram id: {x}")
        url = f"https://{SHOPER_STORE}/webapi/rest/products/{x}"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers)
        res = response.json()
        name = res.get("translations").get("en_GB").get("name")
        art_sku = res.get("code")
        art_ean = res.get("ean")
        price = res.get("stock").get("price")
        description = res.get("translations").get("en_GB").get("description")
        image = res.get("main_image").get("name")
        gfx_id = res.get("main_image").get("gfx_id")
        time.sleep(2)

        print(
            f"{art_sku}:{name}:{art_ean}:{price}:{description}:https://meowbaby.eu/userdata/public/gfx/{gfx_id}/{image}"
        )

    return


# == DEBUGING ==
# print(get_single_product(121))
# print(get_product_images(3596))
