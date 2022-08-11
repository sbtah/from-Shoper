import time
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.helpers.logging import logging


# Simple GET Requests
def get_number_of_product_pages():
    """Return number of product pages from Shoper Api."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, timeout=30, headers=headers)
        time.sleep(0.5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(get_number_of_product_pages) Exception: {e}")
    else:
        res = response.json()
        pages = res.get("pages")
        return pages


def get_number_of_products():
    """Return number of all products in your Shoper store."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, timeout=30, headers=headers)
        time.sleep(0.5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(get_number_of_product_pages) Exception: {e}")
    else:
        res = response.json()
        number = res.get("count")
        return number


def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, timeout=30, headers=headers)
        time.sleep(0.5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(python_get) Exception: {e}")
    else:
        product = response.json()
        return product


def get_all_products():
    """Return a paginated response with all products and number of pages."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, timeout=30, headers=headers)
        time.sleep(0.5)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        logging.error("Connection was timed out.")
        return None
    except requests.exceptions.ConnectionError:
        logging.error("Connection Error.")
        return None
    except requests.exceptions.HTTPError:
        logging.error("HTTPError was raised.")
        return None
    except Exception as e:
        logging.error(f"(python_get) Exception: {e}")
    else:
        products = response.json()
        return products
