import os
import requests
from dotenv import load_dotenv


load_dotenv()
SHOPIFY_STORE = os.environ.get("SHOPIFY_STORE")
SHOPIFY_TOKEN = os.environ.get("SHOPIFY_TOKEN")


url = f"https://{SHOPIFY_STORE}.myshopify.com/admin/api/2022-01/products.json"
payload = {}
headers = {"X-Shopify-Access-Token": f"{SHOPIFY_TOKEN}"}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
