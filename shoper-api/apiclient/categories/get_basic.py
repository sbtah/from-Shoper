import time
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.helpers.logging import logging


def get_number_of_categories_pages():
    """Return number of categories pages from Shoper Api."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.5)
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


def get_number_of_categories():
    """Return number of all Categories from Shoper Api."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.5)
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
        logging.error(f"(get_number_of_categories) Exception: {e}")
    else:
        res = response.json()
        number = res.get("count")
        return number


def get_single_category(id):
    """Return a response with data from single Category endpoint."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.5)
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
        logging.error(f"(get_single_category) Exception: {e}")
    else:
        res = response.json()
        number = res.get("count")
        return number
