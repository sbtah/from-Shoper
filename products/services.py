import requests
import os
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


def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()

    try:
        shoper_title_pl = product.get("translations").get("pl_PL").get("name")
    except AttributeError:
        shoper_title_pl = ""

    try:
        shoper_title_en = product.get("translations").get("en_GB").get("name")
    except AttributeError:
        shoper_title_en = ""

    try:
        shoper_title_de = product.get("translations").get("de_DE").get("name")
    except AttributeError:
        shoper_title_de = ""

    try:
        shoper_title_fr = product.get("translations").get("fr_FR").get("name")
    except AttributeError:
        shoper_title_fr = ""

    try:
        shoper_description_pl = (
            product.get("translations").get("pl_PL").get("description")
        )
    except AttributeError:
        shoper_description_pl = ""

    try:
        shoper_description_en = (
            product.get("translations").get("en_GB").get("description")
        )
    except AttributeError:
        shoper_description_en = ""

    try:
        shoper_description_fr = (
            product.get("translations").get("fr_FR").get("description")
        )
    except AttributeError:
        shoper_description_fr = ""

    try:
        shoper_description_de = (
            product.get("translations").get("de_DE").get("description")
        )
    except AttributeError:
        shoper_description_de = ""

    vendor_brand = SHOPER_STORE[0:-3].capitalize()
    shoper_id = product.get("product_id")

    try:
        shoper_ean = product.get("ean")
    except AttributeError:
        shoper_ean = ""

    try:
        shoper_sku = product.get("code")
    except AttributeError:
        shoper_sku = ""

    try:
        shoper_weight = product.get("vol_weight")
    except AttributeError:
        shoper_weight = ""

    try:
        is_active_shoper = product.get("stock").get("active")
    except AttributeError:
        is_active_shoper = ""

    try:
        created_shoper = product.get("add_date")
    except AttributeError:
        created_shoper = ""

    try:
        updated_shoper = product.get("edit_date")
    except AttributeError:
        updated_shoper = ""

    try:
        is_on_shoper = f'{True if product.get("add_date") else ""}'
    except AttributeError:
        is_on_shoper = ""

    try:
        shoper_price = product.get("stock").get("price")
    except AttributeError:
        shoper_price = ""

    try:
        shoper_gauge_id = product.get("gauge_id")
    except:
        shoper_gauge_id = ""

    return {
        "shoper_title_pl": shoper_title_pl,
        "shoper_title_en": shoper_title_en,
        "shoper_title_de": shoper_title_de,
        "shoper_title_fr": shoper_title_fr,
        "shoper_description_pl": shoper_description_pl,
        "shoper_description_en": shoper_description_en,
        "shoper_description_fr": shoper_description_fr,
        "shoper_description_de": shoper_description_de,
        "vendor_brand": vendor_brand,
        "shoper_id": shoper_id,
        "shoper_ean": shoper_ean,
        "shoper_sku": shoper_sku,
        "shoper_weight": shoper_weight,
        "is_active_shoper": is_active_shoper,
        "created_shoper": created_shoper,
        "updated_shoper": updated_shoper,
        "is_on_shoper": is_on_shoper,
        "shoper_price": shoper_price,
        "shoper_gauge_id": shoper_gauge_id,
    }
