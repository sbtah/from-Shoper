import json
import base64
import time
import requests
from apiclient.helpers.logging import logging
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


def set_new_alt_for_image_translation(gfx_id, alt_of_img, language):
    """
    Set a new name value for ImageTranslation object using Shoper Api.
    """

    data = json.dumps(
        {
            "translations": {
                f"{language}": {
                    "name": f"{alt_of_img}",
                },
            },
        }
    )
    url = f"https://{SHOPER_DOMAIN}/webapi/rest/product-images/{gfx_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.put(url, headers=headers, data=data)
        res = response.json()
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
        logging.error(f"(set_new_alt_for_image_translation) Exception: {e}")
    else:
        res = response.json()
        return res
