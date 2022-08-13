import json
import base64
import time
import logging
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN


# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
        logging.error(f"(get_number_of_image_pages) Exception: {e}")
    else:
        res = response.json()
        pages = res.get("pages")
        return pages


def get_number_of_images():
    """Return number of all images in your Shoper store."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
        logging.error(f"(get_number_of_images) Exception: {e}")
    else:
        res = response.json()
        count = res.get("count")
        return count


def get_single_gfx_image(id):
    """
    Returns a reponse from product images endpoint.
    https://shop.url/webapi/rest/product-images/<id>
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images/{id}"
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
        image = response.json()
        return image


def get_all_images():
    """Return a paginated response with all products and number of pages."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
        logging.error(f"(get_number_of_images) Exception: {e}")
    else:
        images = response.json()
        return images
