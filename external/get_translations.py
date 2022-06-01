import time
import requests
from external.get_token import SHOPER_STORE, TOKEN


# GET Requests
def get_all_translations():
    """Return a paginated response with all translations and number of pages."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product_list = response.json().get("list")

    return product_list


def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()

    return product


def get_single_product_translation_for_language(shoper_id, language_code):
    """Return a response with translation data for single product by language code."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{shoper_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    translation = response.json().get("translations").get(language_code)

    return translation


def get_all_translations_tags_for_product(shoper_id):
    """
    Returns an iterator of language tags active for product in Shoper's Db.
    Api call to product by id endpoint.
    Used for creation of language tags when downloading the data base.
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{shoper_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    data = response.json().get("translations")

    return (tag for tag in data)


# Get all SKU values of products from SHOPER Api.
def get_list_of_all_shoper_product_sku(lang_code):
    """Get all product SKU from SHOPER Api."""

    product_list = []
    # number_of_product_pages = get_number_of_product_pages()

    # #for x in range(1, number_of_product_pages + 1):
    #     data = {"page": f"{x}"}
    #     url = f"https://{SHOPER_STORE}/webapi/rest/products"
    #     headers = {"Authorization": f"Bearer {TOKEN}"}
    #     response = requests.get(url, headers=headers, params=data)
    #     res = response.json()
    #     items = res.get("list")
    #     time.sleep(0.5)
    #     for i in items:
    #         if lang_code in i.get("code"):
    #             product_list.append(i.get("code"))
    #             print(f"SKU:{i.get('code')} - Added to list")

    #         else:
    #             print(f"{i.get('code')}: Passed")

    return product_list
