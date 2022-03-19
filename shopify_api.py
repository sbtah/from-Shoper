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
            "title": "test",
            "body_html": "<h1>TEST</h1>",
            "vendor": "Test vendor",
            "product_type": "ooo",
            "published": "false",
        }
    }
    headers = {
        "X-Shopify-Access-Token": f"{SHOPIFY_TOKEN}",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return response.json()


print(create_product())
