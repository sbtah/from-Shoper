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


def get_all_images():
    """
    Return a reponse with all images
    https://shop.url/webapi/rest/product-images
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


def get_gfx_image_by_id(id):
    """
    Returns a reponse from product images endpoint.
    https://shop.url/webapi/rest/product-images/<id>
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


# Get number of pages from product list API.
def get_number_of_product_pages():
    """Get number of all product pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


# Get all ID numbers of products from SHOPER Api.
def get_list_of_all_shoper_product_ids():
    """Get all product ids from SHOPER Api."""

    product_list = []

    for x in range(1, get_number_of_product_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            product_list.append(int(i.get("product_id")))
            print(f"ID:{i.get('product_id')} - Added to list")
            time.sleep(0.5)

    return product_list


# Get all ID numbers of images from SHOPER Api.
def get_list_of_all_shoper_image_ids():
    """Get all image IDs from SHOPER Api."""

    image_list = []

    for x in range(1, get_number_of_image_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:
            image_list.append(int(i.get("product_id")))
            print(f"GFX_ID:{i.get('product_id')} - Added to list")
            time.sleep(0.5)

    return image_list


def get_product_data_for_shopify(id):
    """Get product data necessary for creation of product in Shopify"""

    print(f"Downloading ID: {id}")
    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    name = res.get("translations").get("en_GB").get("name")
    art_sku = res.get("code")
    art_ean = res.get("ean")
    price = res.get("stock").get("price")
    description = res.get("translations").get("en_GB").get("description")
    main_image = f'https://{SHOPER_STORE}/userdata/public/gfx/{res.get("main_image").get("gfx_id")}/{res.get("main_image").get("name")}'
    images_list = []
    for image in get_list_of_all_shoper_image_ids():
        if image.get("product_id") == id:
            images_list.append(
                f'https://{SHOPER_STORE}/userdata/public/gfx/{res.get("gfx_id")}/{res.get("en_GB").get("name")}.jpg'
            )

    time.sleep(0.5)

    return (
        name,
        art_sku,
        art_ean,
        price,
        description,
        main_image,
        images_list,
    )


# == DEBUGING ==
# print(get_single_product(222))
# print(get_all_images())
# print(get_number_of_product_pages())
# print(get_number_of_image_pages())
# print(get_list_of_all_shoper_image_ids())
print(get_gfx_image_by_id(661))
