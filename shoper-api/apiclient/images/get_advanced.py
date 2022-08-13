import json
import base64
import time
import logging
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.images.get_basic import get_number_of_image_pages


def get_single_image_data(image_id):
    """
    Sends GET request to Shoper's image API endpoint that returns data for single product.
    Properly selects and cleans data from reponse and stores it the variables.
    Variables are used in dictionary that is returned by this function.
    Used for generating copy data of image via Shoper API.
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images/{image_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.3)
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
        logging.error(f"(get_single_image_data) Exception: {e}")
    else:
        image = response.json()
        return image


def from_response_image(response):
    """
    Parses image data from Shoper Api.
    Stores data in proper variables and returns dictionary of needed data for .
    """

    try:
        shoper_gfx_id = response.get("gfx_id")
    except AttributeError:
        shoper_product_id = ""
    try:
        shoper_product_id = response.get("product_id")
    except AttributeError:
        shoper_product_id = ""
    try:
        shoper_main = response.get("main")
    except AttributeError:
        shoper_main = ""
    try:
        shoper_order = response.get("order")
    except AttributeError:
        shoper_order = ""
    try:
        shoper_image_name = response.get("name")
    except AttributeError:
        shoper_image_name = ""
    try:
        shoper_unic = response.get("unic_name")
    except AttributeError:
        shoper_unic = ""
    try:
        shoper_hidden = response.get("hidden")
    except AttributeError:
        shoper_hidden = ""
    try:
        shoper_extension = response.get("extension")
    except AttributeError:
        shoper_extension = ""
    try:
        shoper_image_translations = response.get("translations")
    except AttributeError:
        shoper_image_translations = ""

    return {
        "shoper_gfx_id": shoper_gfx_id,
        "shoper_product_id": shoper_product_id,
        "shoper_main": shoper_main,
        "shoper_order": shoper_order,
        "shoper_image_name": shoper_image_name,
        "shoper_unic": shoper_unic,
        "shoper_hidden": shoper_hidden,
        "shoper_extension": shoper_extension,
        "shoper_image_translations": shoper_image_translations,
    }


def from_response_translations_for_image(response):
    """"""
    try:
        for translation in response.items():
            tag = translation[0]
            shoper_translation_id = translation[1].get("translation_id")
            related_gfx_id = translation[1].get("gfx_id")
            name = translation[1].get("name")
            lang_id = translation[1].get("lang_id")
            yield {
                "locale": tag,
                "shoper_translation_id": shoper_translation_id,
                "related_gfx_id": related_gfx_id,
                "name": name,
                "lang_id": lang_id,
            }
    except Exception as e:
        logging.error(f"Error while getting response: {e}")
