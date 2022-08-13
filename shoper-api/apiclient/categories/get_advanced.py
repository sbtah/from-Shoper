import time
import requests
from apiclient.helpers.get_token import SHOPER_DOMAIN, TOKEN
from apiclient.helpers.logging import logging


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


def from_response_category(response):
    """
    Parses Category response data.
    Stores data in proper variables and returns dictionary of needed data for Category.
    """
    category_id = response.get("category_id")
    root = response.get("root")
    order = response.get("order")
    translations = response.get("translations")

    return {
        "category_id": category_id,
        "root": root,
        "order": order,
        "category_translations": translations,
    }


def from_response_translations_for_category(response):
    """
    Given the part of response from get_single_category_data,
    Yield data for all translations for this Category.

    Used to seperate logic of creating Categories and Translations.
    """
    # print(response)
    # try:
    for translation in response.items():
        # print(translation)
        try:
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
            is_default = translation[1].get("isdefault")
            lang_id = translation[1].get("lang_id")
            items = translation[1].get("items")
            yield {
                "locale": locale,
                "shoper_translation_id": shoper_translation_id,
                "related_category_id": related_category_id,
                "category_name": name,
                "category_description": description,
                "category_description_bottom": description_bottom,
                "category_seo_title": seo_title,
                "category_seo_description": seo_description,
                "category_seo_keywords": seo_keywords,
                "category_seo_url": seo_url,
                "category_permalink": permalink,
                "category_active": active,
                "category_is_default": is_default,
                "category_lang_id": lang_id,
                "category_items": items,
            }
        except Exception as e:
            logging.error(f"Error while getting response: {e}")
