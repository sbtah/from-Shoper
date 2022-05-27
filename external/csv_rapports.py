import time
import requests
from external.token import get_token
from external.token import SHOPER_STORE
from external.get_products import get_list_of_all_shoper_product_ids


TOKEN = get_token()


def get_sku_and_current_url_for_language(id, language_code):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
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

    with open("rapport.csv", "a") as file:
        file.write(
            f"\n{shoper_id};{sku};{sku}{language_code}[:3];{name};{current_link};{seo_link}"
        )

    return shoper_id, sku, name, current_link, seo_link


def generate_product_urls_for_language(language):
    "This can be overriten in context to DJANO for a management command"
    "Generate CSV file with all urls for products for specified language code."

    with open("rapport.csv", "a") as file:
        file.write(f"Shoper ID;SKU;{language}-SKU;NAME;LINK;SEO-LINK")

    for id in get_list_of_all_shoper_product_ids():

        get_sku_and_current_url_for_language(id, language)
        time.sleep(0.5)
