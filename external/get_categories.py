import time
import requests
from external.get_token import SHOPER_STORE, TOKEN


# GET Requests
def get_number_of_categories_pages():
    """Return number of categories pages from Shoper Api."""

    url = f"https://{SHOPER_STORE}/webapi/rest/categories"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        time.sleep(0.5)
        res = response.json()
        pages = res.get("pages")
    except Exception as e:
        print(e)

    return pages


# Get all categories data from SHOPER Api.
def get_all_categories_data():
    """Get all categories from SHOPER Api."""

    number_of_pages = get_number_of_categories_pages()

    for x in range(1, number_of_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/categories"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:

            yield {
                "category_id": i.get("category_id"),
                "root": i.get("root"),
                "order": i.get("order"),
            }
            for tag in i.get("translations"):
                yield {
                    "locale": tag,
                    "name": i.get("translations").get(tag).get("name"),
                    "description": i.get("translations").get(tag).get("description"),
                    "description_bottom": i.get("translations")
                    .get(tag)
                    .get("description_bottom"),
                    "seo_title": i.get("translations").get(tag).get("seo_title"),
                    "seo_description": i.get("translations")
                    .get(tag)
                    .get("seo_description"),
                    "seo_keywords": i.get("translations").get(tag).get("seo_keywords"),
                    "seo_url": i.get("translations").get(tag).get("seo_url"),
                    "permalink": i.get("translations").get(tag).get("permalink"),
                    "dactive": i.get("translations").get(tag).get("active"),
                    "is_default": i.get("translations").get(tag).get("is_default"),
                    "lang_id": i.get("translations").get(tag).get("lang_id"),
                    "items": i.get("translations").get(tag).get("items"),
                }
