import requests
import time
import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand

# from products.models import Product


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


# Get number of pages from product list API.
def get_number_of_product_pages():
    """Get number of all product pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


# Get all ID numbers of products from SHOPER Api.
def copy_all_products_from_shoper_api():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    for x in range(1, get_number_of_product_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")

        for i in items:
            print(i)
            print(
                "==============================================================================="
            )
            title = i.get("translations").get("en_GB").get("name")
            description = i.get("translations").get("en_GB").get("description")
            vendor = "MeowBaby"
            shoper_id = i.get("product_id")

            sku = i.get("code")
            ean = i.get("ean")
            # print(title, description, vendor, shoper_id, sku, ean)
            # print(
            #     "==============================================================================="
            # )
            # Product.objects.create()
            time.sleep(1)

    return


copy_all_products_from_shoper_api()
