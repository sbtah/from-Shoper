import time
import requests
from helpers.get_token import SHOPER_DOMAIN, TOKEN
from external.get_products import get_list_of_all_shoper_product_ids


def get_sku_and_current_url_for_language(id, language_code, file_name):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    try:
        shoper_id = res.get("product_id")
    except AttributeError:
        shoper_id = ""
    try:
        sku = res.get("code")
    except AttributeError:
        sku = ""
    try:
        name = res.get("translations").get(f"{language_code}").get("name")
    except AttributeError:
        name = ""
    try:
        current_link = res.get("translations").get(f"{language_code}").get("permalink")
    except AttributeError:
        current_link = ""
    try:
        seo_link = res.get("translations").get(f"{language_code}").get("seo_url")
    except AttributeError:
        seo_link = ""

    with open(f"{file_name}.csv", "a") as file:
        file.write(f"\n{shoper_id};{sku};{name};{current_link};{seo_link}")

    time.sleep(0.5)
    return shoper_id, sku, name, current_link, seo_link


def get_sku_and_name_for_language(id, language_code, file_name):

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    try:
        sku = res.get("code")
    except AttributeError:
        sku = ""
    try:
        name = res.get("translations").get(f"{language_code}").get("name")
    except AttributeError:
        name = ""

    with open(f"{file_name}.csv", "a") as file:
        file.write(f"\n{sku};{name}")

    time.sleep(0.5)
    return sku, name


# def generate_product_urls_for_language(language):
#     "This can be overriten in context to DJANO for a management command"
#     "Generate CSV file with all urls for products for specified language code."

#     with open("rapport.csv", "a") as file:
#         file.write(f"Shoper ID;SKU;NAME;LINK;SEO-LINK")

#     for id in get_list_of_all_shoper_product_ids():

#         get_sku_and_current_url_for_language(id, language)
#         time.sleep(0.5)


def get_vol_weight_data_of_product(product_id):

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    time.sleep(0.5)
    product = response.json()

    return (
        f'{product.get("code")};{product.get("product_id")};{product.get("vol_weight")}'
    )
