import json
import base64
import time
import logging
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.images.get_basic import get_number_of_image_pages


def get_all_images_data():
    """
    Yield all Images for all pages from Shoper Api,
    by looping over all pages.
    """

    number_of_images_pages = get_number_of_image_pages()
    assert number_of_images_pages, "Number of image pages is None..."

    for x in range(1, number_of_images_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
            logging.error(f"(get_all_images_data) Exception: {e}")
        else:
            res = response.json()
            images = res.get("list")
            try:
                for image in images:
                    yield image
            except TypeError as e:
                logging.error(f"Empty page ? for page nr: {x} : {e}")
                break


def get_all_images_ids():
    """
    Yield all Images IDs for all pages from Shoper Api,
    by looping over all pages.
    """

    number_of_images_pages = get_number_of_image_pages()
    assert number_of_images_pages, "Number of image pages is None..."

    for x in range(1, number_of_images_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images"
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
            logging.error(f"(get_all_images_data) Exception: {e}")
        else:
            res = response.json()
            images = res.get("list")
            try:
                for image in images:
                    logging.info(f"ID: {image.get('gfx_id')} - Found")
                    yield image.get("gfx_id")
            except TypeError as e:
                logging.error(f"Empty page ? for page nr: {x} : {e}")
                break
