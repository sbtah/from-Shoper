import os
import json
import requests
from dotenv import load_dotenv


load_dotenv()
SHOPIFY_STORE = os.environ.get("SHOPIFY_STORE")
SHOPIFY_TOKEN = os.environ.get("SHOPIFY_TOKEN")


def get_products():
    """Get all products from Shopify store."""

    url = f"https://{SHOPIFY_STORE}.myshopify.com/admin/api/2022-01/products.json"
    payload = {}
    headers = {"X-Shopify-Access-Token": f"{SHOPIFY_TOKEN}"}
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def create_product():
    """"""

    url = f"https://{SHOPIFY_STORE}.myshopify.com/admin/api/2022-01/products.json"
    payload = {
        "product": {
            "title": f"test",
            "body_html": f"<h1>TEST</h1>",
            "vendor": f"Test vendor",
            "product_type": f"ooo",
            "published": f"false",
            "images": [
                {
                    "src": f"https://meowbaby.eu/userdata/public/gfx/3593/Gotowy-zestaw-basen-z-kulkami-000230.jpg"
                }
            ],
            "presentment_prices": [
                {
                    "price": {"amount": "0.00", "currency_code": "USD"},
                }
            ],
        }
    }
    headers = {
        "X-Shopify-Access-Token": f"{SHOPIFY_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return response.json()


# == DEBUGING ==
# print(get_products())
# print(create_product())
