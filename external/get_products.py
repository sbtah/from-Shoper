import time
import requests
from external.token import get_token
from external.token import SHOPER_STORE, SHOPER_LOGIN, SHOPER_PASSWORD
from external.create_url import create_seo_url


TOKEN = get_token()


# GET Requests
def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()

    return product


def get_single_product_translation_data(id, language_code):
    """Return a response with translation data for single product by language code."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    translation = response.json().get("translations").get(language_code)

    return translation


def get_all_products():
    """Return a paginated response with all products and number of pages."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


def get_number_of_product_pages():
    """Return number of product pages from Shoper Api."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
        pages = res.get("pages")
    except Exception as e:
        print(e)

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


def get_single_product_data_for_copy(product_id, language_code):
    """
    Used for generating copy data for duplication of product via Shoper API.
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    producer_id = res.get("producer_id")
    category_id = res.get("category_id")
    other_price = res.get("other_price")
    code = res.get("code")
    ean = res.get("ean")
    vol_weight = res.get("vol_weight")
    stock_price = res.get("stock").get("price")
    stock_weight = res.get("stock").get("weight")
    stock_availability_id = res.get("stock").get("availability_id")
    stock_delivery_id = res.get("stock").get("delivery_id")
    stock_gfx_id = res.get("stock").get("gfx_id")
    translations_name = res.get("translations").get(language_code).get("name")
    translations_short_description = (
        res.get("translations").get(language_code).get("short_description")
    )
    try:
        translations_description = (
            res.get("translations").get(language_code).get("description")
        )
    except AttributeError or None:
        translations_description = ""
    try:
        translations_active = res.get("translations").get(language_code).get("active")
    except AttributeError or None:
        translations_active = ""

    time.sleep(0.5)

    return {
        "producer_id": producer_id,
        "category_id": category_id,
        "other_price": other_price,
        "code": code,
        "ean": ean,
        "vol_weight": vol_weight,
        "stock_price": stock_price,
        "stock_weight": stock_weight,
        "stock_availability_id": stock_availability_id,
        "stock_delivery_id": stock_delivery_id,
        "stock_gfx_id": stock_gfx_id,
        "translations_name": translations_name,
        "translations_short_description": translations_short_description,
        "translations_description": translations_description,
        "translations_active": translations_active,
    }


def create_seo_url_and_create_redirect_to_it():
    pass
