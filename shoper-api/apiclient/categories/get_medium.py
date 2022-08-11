import time
import requests
from shoper_api.helpers.get_token import SHOPER_DOMAIN, TOKEN
from shoper_api.helpers.logging import logging
from shoper_api.categories.get_basic import get_number_of_categories_pages


def get_all_category_data():
    """
    Yield all Categories for all pages from Shoper Api,
    by looping over all pages.
    """

    number_of_product_pages = get_number_of_categories_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
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
            logging.error(f"(get_all_category_data) Exception: {e}")
        else:
            res = response.json()
            categories = res.get("list")
            try:
                for category in categories:
                    yield category
            except TypeError as e:
                print(f"Empty page ? for page nr: {x} : {e}")
                break


# Get all ID numbers of products from SHOPER Api.
def get_all_shoper_categories_ids():
    """
    Yield all Category IDs in your Shoper store.
    """

    number_of_product_pages = get_number_of_categories_pages()
    assert number_of_product_pages, "Number of product pages is None..."

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
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
            categories = res.get("list")
            try:
                for category in categories:
                    logging.info(f"ID: {category.get('category_id')} - Found")
                    yield category.get("category_id")

            except Exception as e:
                logging.error(f"Some nasty exception : {e}")
                break
