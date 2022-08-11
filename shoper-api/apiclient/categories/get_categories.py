import time
import requests
from helpers.get_token import SHOPER_DOMAIN, TOKEN


# GET Requests
def get_number_of_categories_pages():
    """Return number of categories pages from Shoper Api."""

    url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
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
        url = f"https://{SHOPER_DOMAIN}/webapi/rest/categories"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:

            yield i
