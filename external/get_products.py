import time
import requests
from external.get_token import SHOPER_STORE, TOKEN


# GET Requests
def get_number_of_product_pages():
    """Return number of product pages from Shoper Api."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        res = response.json()
        pages = res.get("pages")
    except Exception as e:
        print(e)

    return pages


def get_single_product(id):
    """Return a response with data from single product endpoint."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    product = response.json()
    time.sleep(0.5)

    return product


def get_all_products():
    """Return a paginated response with all products and number of pages."""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()

    return res


def get_all_products_data():
    """Get all Products for all pages from Shoper Api."""

    number_of_product_pages = get_number_of_product_pages()

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        time.sleep(0.5)
        res = response.json()
        items = res.get("list")
        try:
            for i in items:
                yield i
        except TypeError as e:
            print(f"Empty page ? for page nr: {x}")
            pass

# Get all ID numbers of products from SHOPER Api.
def get_list_of_all_shoper_product_ids():
    """Get all product ids from SHOPER Api."""

    product_list = []
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            product_list.append(int(i.get("product_id")))
            print(f"ID:{i.get('product_id')} - Added to list")

    return product_list


def get_list_of_all_shoper_product_ids_for_lang(lang_code):
    """Get all product ids from SHOPER Api."""

    product_list = []
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            if lang_code in i.get("code"):
                product_list.append(int(i.get("product_id")))
                print(f"ID:{i.get('product_id')} - Added to list")
            else:
                print(f"{i.get('code')}: Passed")

    return product_list


# Get all SKU values of products from SHOPER Api.
def get_list_of_all_shoper_product_sku(lang_code):
    """Get all product SKU for picked language, from SHOPER Api."""

    product_list = []
    number_of_product_pages = get_number_of_product_pages()
    print(f"Response pages to get: {number_of_product_pages}")

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        time.sleep(0.5)
        for i in items:
            if lang_code in i.get("code"):
                print(i.get("code"))
                product_list.append(i.get("code"))
                print(f"SKU:{i.get('code')} - Added to list")

            else:
                print(f"{i.get('code')}: Passed")

    return product_list


def get_single_product_data(product_id):
    """
    Sends GET request to Shoper's product API endpoint that returns data for single product.
    Properly selects and cleans data from reponse and stores it the variables.
    Variables are used in dictionary that is returned by this function.
    Used for generating copy data for duplication of product via Shoper API.
    """

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    time.sleep(0.5)
    i = response.json()
    try:
        shoper_id = i.get("product_id")
    except AttributeError:
        shoper_id = ""
    try:
        shoper_type = i.get("type")
    except AttributeError:
        shoper_type = None
    try:
        shoper_producer_id = i.get("producer_id")
    except AttributeError:
        shoper_producer_id = None
    try:
        shoper_group_id = i.get("group_id")
    except AttributeError:
        shoper_group_id = None
    try:
        shoper_tax_id = i.get("tax_id")
    except AttributeError:
        shoper_tax_id = None
    try:
        shoper_main_category_id = i.get("category_id")
    except AttributeError:
        shoper_main_category_id = None
    try:
        shoper_all_categories_ids = i.get("categories")
    except AttributeError:
        shoper_all_categories_ids = []
    try:
        shoper_unit_id = i.get("unit_id")
    except AttributeError:
        shoper_unit_id = None
    try:
        created_shoper = i.get("add_date")
    except AttributeError:
        created_shoper = ""
    try:
        updated_shoper = i.get("edit_date")
    except AttributeError:
        updated_shoper = ""
    try:
        shoper_other_price = i.get("other_price")
    except AttributeError:
        shoper_other_price = ""
    try:
        shoper_promo_price = i.get("promo_price")
    except AttributeError:
        shoper_promo_price = ""
    try:
        shoper_sku = i.get("code")
    except AttributeError:
        shoper_sku = ""
    try:
        shoper_ean = i.get("ean")
    except AttributeError:
        shoper_ean = ""
    try:
        shoper_pkwiu = i.get("pkwiu")
    except AttributeError:
        shoper_pkwiu = ""
    try:
        shoper_is_product_of_day = i.get("is_product_of_day")
    except AttributeError:
        shoper_is_product_of_day = ""
    try:
        shoper_bestseller_tag = i.get("bestseller")
    except AttributeError:
        shoper_bestseller_tag = ""
    try:
        shoper_new_product_tag = i.get("newproduct")
    except AttributeError:
        shoper_new_product_tag = ""
    try:
        shoper_vol_weight = i.get("vol_weight")
    except AttributeError:
        shoper_vol_weight = ""
    try:
        shoper_gauge_id = i.get("gauge_id")
    except AttributeError:
        shoper_gauge_id = None
    try:
        shoper_currency_id = i.get("currency_id")
    except AttributeError:
        shoper_currency_id = None
    # Shoper Special Offer.
    try:
        shoper_promo_id = i.get("special_offer").get("promo_id")
    except AttributeError:
        shoper_promo_id = None
    try:
        shoper_promo_start = i.get("special_offer").get("date_from")
    except AttributeError:
        shoper_promo_start = ""
    try:
        shoper_promo_ends = i.get("special_offer").get("date_to")
    except AttributeError:
        shoper_promo_ends = ""
    try:
        shoper_discount_value = i.get("special_offer").get("discount")
    except AttributeError:
        shoper_discount_value = ""

    yield {
        "shoper_id": shoper_id,
        "shoper_type": shoper_type,
        "shoper_producer_id": shoper_producer_id,
        "shoper_group_id": shoper_group_id,
        "shoper_tax_id": shoper_tax_id,
        "shoper_main_category_id": shoper_main_category_id,
        "shoper_all_categories_ids": shoper_all_categories_ids,
        "shoper_unit_id": shoper_unit_id,
        "created_shoper": created_shoper,
        "updated_shoper": updated_shoper,
        "shoper_other_price": shoper_other_price,
        "shoper_promo_price": shoper_promo_price,
        "shoper_sku": shoper_sku,
        "shoper_ean": shoper_ean,
        "shoper_pkwiu": shoper_pkwiu,
        "shoper_is_product_of_day": shoper_is_product_of_day,
        "shoper_bestseller_tag": shoper_bestseller_tag,
        "shoper_new_product_tag": shoper_new_product_tag,
        "shoper_vol_weight": shoper_vol_weight,
        "shoper_gauge_id": shoper_gauge_id,
        "shoper_currency_id": shoper_currency_id,
        "shoper_promo_id": shoper_promo_id,
        "shoper_promo_start": shoper_promo_start,
        "shoper_promo_ends": shoper_promo_ends,
        "shoper_discount_value": shoper_discount_value,
    }
    for locale in i.get("translations"):
        locale = locale
        shoper_translation_id = (
            i.get("translations").get(f"{locale}").get("translation_id")
        )
        related_product_id = i.get("translations").get(f"{locale}").get("product_id")
        name = i.get("translations").get(f"{locale}").get("name")
        short_description = (
            i.get("translations").get(f"{locale}").get("short_description")
        )
        description = i.get("translations").get(f"{locale}").get("description")
        active = i.get("translations").get(f"{locale}").get("active")
        is_default = i.get("translations").get(f"{locale}").get("isdefault")
        lang_id = i.get("translations").get(f"{locale}").get("lang_id")
        seo_title = i.get("translations").get(f"{locale}").get("seo_title")
        seo_description = i.get("translations").get(f"{locale}").get("seo_description")
        seo_keywords = i.get("translations").get(f"{locale}").get("seo_keywords")
        seo_url = i.get("translations").get(f"{locale}").get("seo_url")
        permalink = i.get("translations").get(f"{locale}").get("permalink")
        order = i.get("translations").get(f"{locale}").get("order")
        main_page = i.get("translations").get(f"{locale}").get("main_page")
        main_page_order = i.get("translations").get(f"{locale}").get("main_page_order")

        yield {
            "locale": locale,
            "shoper_translation_id": shoper_translation_id,
            "related_product_id": related_product_id,
            "name": name,
            "short_description": short_description,
            "description": description,
            "active": active,
            "is_default": is_default,
            "lang_id": lang_id,
            "seo_title": seo_title,
            "seo_description": seo_description,
            "seo_keywords": seo_keywords,
            "seo_url": seo_url,
            "permalink": permalink,
            "order": order,
            "main_page": main_page,
            "main_page_order": main_page_order,
        }


# CSV Output
def get_vol_weight_data_of_product(product_id):

    url = f"https://{SHOPER_STORE}/webapi/rest/products/{product_id}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    time.sleep(0.5)
    product = response.json()

    return (
        f'{product.get("code")};{product.get("product_id")};{product.get("vol_weight")}'
    )
