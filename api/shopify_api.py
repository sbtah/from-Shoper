import os
import json
import requests
from dotenv import load_dotenv


load_dotenv()
SHOPIFY_STORE = os.environ.get("SHOPIFY_STORE")
SHOPIFY_TOKEN = os.environ.get("SHOPIFY_TOKEN")
SHOPER_STORE = os.environ.get("SHOPER_STORE")


def get_products():
    """Get all products from Shopify store."""

    url = f"https://{SHOPIFY_STORE}.myshopify.com/admin/api/2022-01/products.json"
    payload = {}
    headers = {"X-Shopify-Access-Token": f"{SHOPIFY_TOKEN}"}
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


# for product in products:

#     product.create_product()

# if model method?
def create_product_at_shopify(self):
    """"""

    list_of_images = []
    for image in self.images:
        list_of_images.append(
            {
                "id": f"product_id",
                "product_id": 1071559598,
                "position": 1,
                "alt": f"ttesdfsdf",
                "src": f"https:/{SHOPER_STORE}/userdata/public/gfx/{image.gfx_id}/{image.name}",
            },
        )

    url = f"https://{SHOPIFY_STORE}.myshopify.com/admin/api/2022-01/products.json"
    payload = {
        "product": {
            "title": f"{self}",
            "body_html": f"{self}",
            "vendor": f"{self}",
            "product_type": f"{self}",
            "published": f"{self}",
            "images": list_of_images,
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
    # shoper_product = self.objects.get(sku=payload.get("product").get("sku"))

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    # self.save(
    #     field=response.get("product").get("sku"),
    # )
    return response.json()


# == DEBUGING ==
print(get_products())
# print(create_product())

# [
#     {
#         "src": f"https:/{SHOPER_STORE}/userdata/public/gfx/3593/Gotowy-zestaw-basen-z-kulkami-000230.jpg"
#     }
# ],
