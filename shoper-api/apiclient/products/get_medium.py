import time
import requests
from apiclient.helpers.logging import logging
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.products.get_basic import get_number_of_product_pages


def get_all_products_data():
    """
    Yield all Products for all pages from Shoper Api,
    by looping over all pages.
    """

    number_of_product_pages = get_number_of_product_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        try:
            response = requests.get(url, headers=headers, params=data)
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
            logging.error(f"(get_all_products_data) Exception: {e}")
        else:
            res = response.json()
            products = res.get("list")
            try:
                for product in products:
                    yield product
            except TypeError as e:
                print(f"Empty page ? for page nr: {x} : {e}")
                break


# Get all ID numbers of products from SHOPER Api.
def get_all_shoper_product_ids():
    """
    Yield all Product IDs in your Shoper store.
    """

    number_of_product_pages = get_number_of_product_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        try:
            response = requests.get(url, headers=headers, params=data)
            time.sleep(0.3)
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
            logging.error(f"(get_all_products_data) Exception: {e}")
        else:
            res = response.json()
            products = res.get("list")
            try:
                for product in products:
                    logging.info(f"ID: {product.get('product_id')} - Found")
                    yield product.get("product_id")

            except Exception as e:
                logging.error(f"Some nasty exception : {e}")
                break


# Get all  numbers of products from SHOPER Api.
def get_all_shoper_product_skus():
    """
    Yield all Product SKU code in your Shoper store.
    """

    number_of_product_pages = get_number_of_product_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        try:
            response = requests.get(url, headers=headers, params=data)
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
            logging.error(f"(get_all_products_data) Exception: {e}")
        else:
            res = response.json()
            products = res.get("list")
            try:
                for product in products:
                    yield product.get("code")
                    logging.info(f"SKU: {product.get('code')} - Found")
            except Exception as e:
                logging.error(f"Some nasty exception : {e}")
                break
