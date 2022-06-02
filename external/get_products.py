import time
import requests
from external.get_token import SHOPER_STORE, TOKEN


# GET Requests
def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()

    return product


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
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            product_list.append(int(i.get("product_id")))
            print(f"ID:{i.get('product_id')} - Added to list")

    return product_list


def get_list_of_all_shoper_product_ids_for_lang(lang_code):
    """Get all product ids from SHOPER Api."""

    product_list = []
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            if lang_code in i.get("code"):
                product_list.append(int(i.get("product_id")))
                print(f"ID:{i.get('product_id')} - Added to list")
            else:
                print(f"{i.get('code')}: Passed")

    return product_list


# Get all SKU values of products from SHOPER Api.
def get_list_of_all_shoper_product_sku(lang_code):
    """Get all product SKU for picked language, from SHOPER Api."""

    product_list = []
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            if lang_code in i.get("code"):
                print(i.get("code"))
                product_list.append(i.get("code"))
                print(f"SKU:{i.get('code')} - Added to list")

            else:
                print(f"{i.get('code')}: Passed")

    return product_list


def get_single_product_data_for_copy(product_id, language_code):
    """
    NOT USED IN ANY DJANGO LOGIC.
    Sends GET request to Shoper's product API endpoint that returns data for single product.
    Properly selects and cleans data from reponse and store it the variables.
    Variables are used in dictionary that is returned by this function.
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
    try:
        translations_short_description = (
            res.get("translations").get(language_code).get("short_description")
        )
    except AttributeError:
        translations_short_description = ""
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


# CSV Output
def get_vol_weight_data_of_product(product_id):

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()

    return f'{product["code"]};{product["product_id"]};{product["vol_weight"]}'
