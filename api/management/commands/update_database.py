import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from images.models import Image
from products.models import Product


# Get private data fron .env variable
load_dotenv()
SHOPER_LOGIN = os.environ.get("SHOPER_LOGIN")
SHOPER_PASSWORD = os.environ.get("SHOPER_PASSWORD")
SHOPER_STORE = os.environ.get("SHOPER_STORE")


# Get a token by login to your store.
def get_token():
    """Generates fresh token from SHOPER API."""

    url_login = f"https://{SHOPER_STORE}/webapi/rest/auth"
    response = requests.post(url_login, auth=(SHOPER_LOGIN, SHOPER_PASSWORD))
    access_token = response.json().get("access_token")
    return access_token


# Get instance of TOKEN.
TOKEN = get_token()


# IMAGES
# Get number of pages from image list API.
def get_number_of_image_pages():
    """Get number of all image pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


def copy_all_product_images_from_shoper_api():
    """Copy all images from SHOPER Api and saves them as Image objects in DB."""

    for x in range(1, get_number_of_image_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        for i in items:

            shoper_gfx_id = i.get("gfx_id")

            try:
                shoper_product_id = i.get("product_id")
            except AttributeError:
                shoper_product_id = ""

            try:
                shoper_main = i.get("main")
            except AttributeError:
                shoper_main = ""

            try:
                shoper_title_pl = i.get("translations").get("pl_PL").get("name")
            except AttributeError:
                shoper_title_pl = ""

            try:
                shoper_title_en = i.get("translations").get("en_GB").get("name")
            except AttributeError:
                shoper_title_en = ""

            try:
                shoper_title_de = i.get("translations").get("de_DE").get("name")
            except AttributeError:
                shoper_title_de = ""

            try:
                shoper_title_fr = i.get("translations").get("fr_FR").get("name")
            except AttributeError:
                shoper_title_fr = ""

            try:
                shoper_order = i.get("order")
            except AttributeError:
                shoper_order = ""

            try:
                shoper_link_pl = f'https://{SHOPER_STORE}/userdata/public/gfx/{i.get("gfx_id")}/{shoper_title_pl[:-4] if ".jpg" in shoper_title_pl else shoper_title_pl}.jpg'
            except AttributeError:
                shoper_link_pl = ""

            try:
                shoper_link_en = f'https://{SHOPER_STORE}/userdata/public/gfx/{i.get("gfx_id")}/{shoper_title_en[:-4] if ".jpg" in shoper_title_en else shoper_title_en}.jpg'
            except AttributeError:
                shoper_link_en = ""

            try:
                shoper_link_de = f'https://{SHOPER_STORE}/userdata/public/gfx/{i.get("gfx_id")}/{shoper_title_de[:-4] if ".jpg" in shoper_title_de else shoper_title_de}.jpg'
            except AttributeError:
                shoper_link_de = ""

            try:
                shoper_link_fr = f'https://{SHOPER_STORE}/userdata/public/gfx/{i.get("gfx_id")}/{shoper_title_fr[:-4] if ".jpg" in shoper_title_fr else shoper_title_fr}.jpg'
            except AttributeError:
                shoper_link_fr = ""

            try:
                shoper_unic = i.get("unic_name")
            except AttributeError:
                shoper_unic = ""

            try:
                shoper_hidden = i.get("hidden")
                # i.get("hidden")
            except AttributeError:
                shoper_hidden = ""

            try:
                shoper_extension = i.get("extension")
            except AttributeError:
                shoper_extension = ""

            try:
                image = Image.objects.get(
                    shoper_gfx_id=shoper_gfx_id,
                )
                if (
                    (str(image.shoper_gfx_id) != str(shoper_gfx_id))
                    or (str(image.shoper_product_id) != str(shoper_product_id))
                    or (str(image.shoper_main) != str(shoper_main))
                    or (str(image.shoper_title_pl) != str(shoper_title_pl))
                    or (str(image.shoper_title_en) != str(shoper_title_en))
                    or (str(image.shoper_title_de) != str(shoper_title_de))
                    or (str(image.shoper_title_fr) != str(shoper_title_fr))
                    or (str(image.shoper_order) != str(shoper_order))
                    or (str(image.shoper_link_pl) != str(shoper_link_pl))
                    or (str(image.shoper_link_en) != str(shoper_link_en))
                    or (str(image.shoper_link_de) != str(shoper_link_de))
                    or (str(image.shoper_link_fr) != str(shoper_link_fr))
                    or (str(image.shoper_unic) != str(shoper_unic))
                    or (str(image.shoper_hidden) != str(shoper_hidden))
                    or (str(image.shoper_extension) != str(shoper_extension))
                ):
                    image.shoper_gfx_id = shoper_gfx_id
                    image.shoper_product_id = shoper_product_id
                    image.shoper_main = shoper_main
                    image.shoper_title_pl = shoper_title_pl
                    image.shoper_title_en = shoper_title_en
                    image.shoper_title_de = shoper_title_de
                    image.shoper_title_fr = shoper_title_fr
                    image.shoper_order = shoper_order

                    image.shoper_link_pl = shoper_link_pl
                    image.shoper_link_en = shoper_link_en
                    image.shoper_link_de = shoper_link_de
                    image.shoper_link_fr = shoper_link_fr
                    image.shoper_unic = shoper_unic
                    image.shoper_hidden = shoper_hidden

                    image.shoper_extension = shoper_extension
                    image.save()
                    print(f"UPDATED: {image}")
                else:
                    print(f"No update detected for: {image}")
            except Image.DoesNotExist:
                Image.objects.create(
                    shoper_gfx_id=shoper_gfx_id,
                    shoper_product_id=shoper_product_id,
                    shoper_main=shoper_main,
                    shoper_title_pl=shoper_title_pl,
                    shoper_title_en=shoper_title_en,
                    shoper_title_de=shoper_title_de,
                    shoper_title_fr=shoper_title_fr,
                    shoper_order=shoper_order,
                    shoper_link_pl=shoper_link_pl,
                    shoper_link_en=shoper_link_en,
                    shoper_link_de=shoper_link_de,
                    shoper_link_fr=shoper_link_fr,
                    shoper_unic=shoper_unic,
                    shoper_hidden=shoper_hidden,
                    shoper_extension=shoper_extension,
                )
                print(f"CREATED: {Image}")
            time.sleep(1)
    return


# PRODUCTS
# Get number of pages from product list API.
def get_number_of_product_pages():
    """Get number of all product pages from SHOPER api"""

    url = f"https://{SHOPER_STORE}/webapi/rest/products"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response = requests.get(url, headers=headers)
    res = response.json()
    pages = res.get("pages")

    return pages


# Get all ID numbers of products from SHOPER Api.
def copy_all_products_from_shoper_api():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    for x in range(1, get_number_of_product_pages() + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")

        for i in items:
            # Shoper Main Data
            try:
                shoper_id = i.get("product_id")
            except AttributeError:
                shoper_id = ""
            try:
                shoper_ean = i.get("ean")
            except AttributeError:
                shoper_ean = ""
            try:
                shoper_sku = i.get("code")
            except AttributeError:
                shoper_sku = ""
            try:
                shoper_weight = i.get("vol_weight")
            except AttributeError:
                shoper_weight = ""
            try:
                is_active_shoper = i.get("stock").get("active")  # Test it!
            except AttributeError:
                is_active_shoper = ""
            try:
                vendor_brand = SHOPER_STORE[0:-3].capitalize()
            except AttributeError:
                vendor_brand = ""
            try:
                created_shoper = i.get("add_date")
            except AttributeError:
                created_shoper = ""
            try:
                updated_shoper = i.get("edit_date")
            except AttributeError:
                updated_shoper = ""
            try:
                shoper_price = i.get("stock").get("price")
            except AttributeError:
                shoper_price = ""
            try:
                shoper_gauge_id = i.get("gauge_id")
            except AttributeError:
                shoper_gauge_id = ""
            try:
                shoper_discount_value = i.get("special_offer").get("discount")
            except AttributeError:
                shoper_discount_value = ""
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
                shoper_bestseller_tag = i.get("bestseller")
            except AttributeError:
                shoper_bestseller_tag = ""
            try:
                shoper_new_product_tag = i.get("newproduct")
            except AttributeError:
                shoper_new_product_tag = ""

            # Titles all languages.
            try:
                shoper_title_pl = i.get("translations").get("pl_PL").get("name")
            except AttributeError:
                shoper_title_pl = ""
            try:
                shoper_title_en = i.get("translations").get("en_GB").get("name")
            except AttributeError:
                shoper_title_en = ""
            try:
                shoper_title_de = i.get("translations").get("de_DE").get("name")
            except AttributeError:
                shoper_title_de = ""
            try:
                shoper_title_fr = i.get("translations").get("fr_FR").get("name")
            except AttributeError:
                shoper_title_fr = ""
            # PL SEO DATA
            try:
                shoper_description_pl = (
                    i.get("translations").get("pl_PL").get("description")
                )
            except AttributeError:
                shoper_description_pl = ""
            try:
                shoper_seo_title_pl = (
                    i.get("translations").get("pl_PL").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_pl = ""
            try:
                shoper_meta_desc_pl = (
                    i.get("translations").get("pl_PL").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_pl = ""
            try:
                shoper_permalink_pl = (
                    i.get("translations").get("pl_PL").get("permalink")
                )
            except AttributeError:
                shoper_permalink_pl = ""
            try:
                shoper_seo_url_pl = i.get("translations").get("pl_PL").get("seo_url")
            except AttributeError:
                shoper_seo_url_pl = ""
            # EN SEO DATA
            try:
                shoper_description_en = (
                    i.get("translations").get("en_GB").get("description")
                )
            except AttributeError:
                shoper_description_en = ""
            try:
                shoper_seo_title_en = (
                    i.get("translations").get("en_GB").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_en = ""
            try:
                shoper_meta_desc_en = (
                    i.get("translations").get("en_GB").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_en = ""
            try:
                shoper_permalink_en = (
                    i.get("translations").get("en_GB").get("permalink")
                )
            except AttributeError:
                shoper_permalink_en = ""
            try:
                shoper_seo_url_en = i.get("translations").get("en_GB").get("seo_url")
            except AttributeError:
                shoper_seo_url_en = ""
            # FR SEO DATA
            try:
                shoper_description_fr = (
                    i.get("translations").get("fr_FR").get("description")
                )
            except AttributeError:
                shoper_description_fr = ""
            try:
                shoper_seo_title_fr = (
                    i.get("translations").get("fr_FR").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_fr = ""
            try:
                shoper_meta_desc_fr = (
                    i.get("translations").get("fr_FR").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_fr = ""
            try:
                shoper_permalink_fr = (
                    i.get("translations").get("fr_FR").get("permalink")
                )
            except AttributeError:
                shoper_permalink_fr = ""
            try:
                shoper_seo_url_fr = i.get("translations").get("fr_FR").get("seo_url")
            except AttributeError:
                shoper_seo_url_fr = ""
            # DE SEO DATA
            try:
                shoper_description_de = (
                    i.get("translations").get("de_DE").get("description")
                )
            except AttributeError:
                shoper_description_de = ""
            try:
                shoper_seo_title_de = (
                    i.get("translations").get("de_DE").get("seo_title")
                )
            except AttributeError:
                shoper_seo_title_de = ""
            try:
                shoper_meta_desc_de = (
                    i.get("translations").get("de_DE").get("seo_description")
                )
            except AttributeError:
                shoper_meta_desc_de = ""
            try:
                shoper_permalink_de = (
                    i.get("translations").get("de_DE").get("permalink")
                )
            except AttributeError:
                shoper_permalink_de = ""
            try:
                shoper_seo_url_de = i.get("translations").get("de_DE").get("seo_url")
            except AttributeError:
                shoper_seo_url_de = ""
            try:
                product = Product.objects.get(
                    shoper_sku=shoper_sku,
                )
                if datetime.strptime(
                    updated_shoper, "%Y-%m-%d %H:%M:%S"
                ) > datetime.strptime(product.updated_shoper, "%Y-%m-%d %H:%M:%S"):
                    # Shoper Main Data
                    product.shoper_id = shoper_id
                    product.shoper_ean = shoper_ean
                    product.shoper_sku = shoper_sku
                    product.shoper_weight = shoper_weight
                    product.is_active_shoper = is_active_shoper
                    product.vendor_brand = vendor_brand
                    product.created_shoper = created_shoper
                    product.updated_shoper = updated_shoper
                    product.shoper_price = shoper_price
                    product.shoper_gauge_id = shoper_gauge_id
                    product.shoper_discount_value = shoper_discount_value
                    product.shoper_promo_id = shoper_promo_id
                    product.shoper_promo_start = shoper_promo_start
                    product.shoper_promo_ends = shoper_promo_ends
                    product.shoper_bestseller_tag = shoper_bestseller_tag
                    product.shoper_new_product_tag = shoper_new_product_tag
                    # Titles all languages.
                    product.shoper_title_pl = shoper_title_pl
                    product.shoper_title_en = shoper_title_en
                    product.shoper_title_de = shoper_title_de
                    product.shoper_title_fr = shoper_title_fr
                    # PL SEO DATA
                    product.shoper_description_pl = shoper_description_pl
                    product.shoper_seo_title_pl = shoper_seo_title_pl
                    product.shoper_meta_desc_pl = shoper_meta_desc_pl
                    product.shoper_permalink_pl = shoper_permalink_pl
                    product.shoper_seo_url_pl = shoper_seo_url_pl
                    # EN SEO DATA
                    product.shoper_description_en = shoper_description_en
                    product.shoper_seo_title_en = shoper_seo_title_en
                    product.shoper_meta_desc_en = shoper_meta_desc_en
                    product.shoper_permalink_en = shoper_permalink_en
                    product.shoper_seo_url_en = shoper_seo_url_en
                    # FR SEO DATA
                    product.shoper_description_fr = shoper_description_fr
                    product.shoper_seo_title_fr = shoper_seo_title_fr
                    product.shoper_meta_desc_fr = shoper_meta_desc_fr
                    product.shoper_permalink_fr = shoper_permalink_fr
                    product.shoper_seo_url_fr = shoper_seo_url_fr
                    # DE SEO DATA
                    product.shoper_description_de = shoper_description_de
                    product.shoper_seo_title_de = shoper_seo_title_de
                    product.shoper_meta_desc_de = shoper_meta_desc_de
                    product.shoper_permalink_de = shoper_permalink_de
                    product.shoper_seo_url_de = shoper_seo_url_de
                    product.save()
                    print(f"UPDATED: {product}")
                else:
                    print(f"No update detected for: {product}")
                    continue
            except Product.DoesNotExist:
                Product.objects.create(
                    # Shoper Main Data
                    shoper_id=shoper_id,
                    shoper_ean=shoper_ean,
                    shoper_sku=shoper_sku,
                    shoper_weight=shoper_weight,
                    is_active_shoper=is_active_shoper,
                    vendor_brand=vendor_brand,
                    created_shoper=created_shoper,
                    updated_shoper=updated_shoper,
                    shoper_price=shoper_price,
                    shoper_gauge_id=shoper_gauge_id,
                    shoper_discount_value=shoper_discount_value,
                    shoper_promo_id=shoper_promo_id,
                    shoper_promo_start=shoper_promo_start,
                    shoper_promo_ends=shoper_promo_ends,
                    shoper_bestseller_tag=shoper_bestseller_tag,
                    shoper_new_product_tag=shoper_new_product_tag,
                    # Titles all languages.
                    shoper_title_pl=shoper_title_pl,
                    shoper_title_en=shoper_title_en,
                    shoper_title_de=shoper_title_de,
                    shoper_title_fr=shoper_title_fr,
                    # PL SEO DATA
                    shoper_description_pl=shoper_description_pl,
                    shoper_seo_title_pl=shoper_seo_title_pl,
                    shoper_meta_desc_pl=shoper_meta_desc_pl,
                    shoper_permalink_pl=shoper_permalink_pl,
                    shoper_seo_url_pl=shoper_seo_url_pl,
                    # EN SEO DATA
                    shoper_description_en=shoper_description_en,
                    shoper_seo_title_en=shoper_seo_title_en,
                    shoper_meta_desc_en=shoper_meta_desc_en,
                    shoper_permalink_en=shoper_permalink_en,
                    shoper_seo_url_en=shoper_seo_url_en,
                    # FR SEO DATA
                    shoper_description_fr=shoper_description_fr,
                    shoper_seo_title_fr=shoper_seo_title_fr,
                    shoper_meta_desc_fr=shoper_meta_desc_fr,
                    shoper_permalink_fr=shoper_permalink_fr,
                    shoper_seo_url_fr=shoper_seo_url_fr,
                    # DE SEO DATA
                    shoper_description_de=shoper_description_de,
                    shoper_seo_title_de=shoper_seo_title_de,
                    shoper_meta_desc_de=shoper_meta_desc_de,
                    shoper_permalink_de=shoper_permalink_de,
                    shoper_seo_url_de=shoper_seo_url_de,
                )
                print(f"CREATED: {Product}")
            time.sleep(1)
    return


def clear_database():
    """
    Clears Images and Products from DB.
    Used for testing.
    """

    Image.objects.all().delete()
    Product.objects.all().delete()


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Database update started!
                Number of Products: {Product.objects.all().count()}
                Number of Images: {Image.objects.all().count()}
                """
            )
        )
        copy_all_product_images_from_shoper_api()
        copy_all_products_from_shoper_api()
        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Database available!
        Number of Products: {Product.objects.all().count()}
        Number of Images: {Image.objects.all().count()}
        """
            )
        )
