import time
import requests
from shoper_api.helpers.get_token import SHOPER_DOMAIN, TOKEN
from shoper_api.helpers.logging import logging


def get_single_category_data(cat_id):
    """
    Sends GET request to Shoper's category API endpoint that returns data for single category.
    Properly selects and cleans data from reponse and stores it the variables.
    Variables are used in dictionary that is returned by this function.
    Used for generating copy data for duplication of category via Shoper API.
    """

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories/{cat_id}"
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
        logging.error(f"(get_single_product_data) Exception: {e}")
    else:
        i = response.json()

        category_id = i.get("category_id")
        root = i.get("root")
        order = i.get("order")
        translations = i.get("translations")

        return {
            "shoper_id": category_id,
            "root": root,
            "order": order,
            "shoper_category_translations": translations,
        }


def from_response_translations_for_category(response):
    """
    Given the part of response from get_single_category_data,
    Yield data for all translations for this Category.

    Used to seperate logic of creating Categories and Translations.
    """
    try:
        for translation in response.items():
            locale = translation[0]
            shoper_translation_id = translation[1].get("trans_id")
            related_category_id = translation[1].get("category_id")
            name = translation[1].get("name")
            description = translation[1].get("description")
            description_bottom = translation[1].get("description_bottom")
            seo_title = translation[1].get("seo_title")
            seo_description = translation[1].get("seo_description")
            seo_keywords = translation[1].get("seo_keywords")
            seo_url = translation[1].get("seo_url")
            permalink = translation[1].get("permalink")
            active = translation[1].get("active")
            is_default = translation[1].get("is_default")
            lang_id = translation[1].get("lang_id")
            items = translation[1].get("items")
        yield {
            "locale": locale,
            "shoper_translation_id": shoper_translation_id,
            "related_category_id": related_category_id,
            "name": name,
            "description": description,
            "description_bottom": description_bottom,
            "seo_title": seo_title,
            "seo_description": seo_description,
            "seo_keywords": seo_keywords,
            "seo_url": seo_url,
            "permalink": permalink,
            "active": active,
            "is_default": is_default,
            "lang_id": lang_id,
            "items": items,
        }
    except Exception as e:
        logging.error(f"Error while getting response: {e}")
