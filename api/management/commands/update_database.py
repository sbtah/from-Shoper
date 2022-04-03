import requests
import time
import os
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
                order = i.get("order")
            except AttributeError:
                order = ""

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
                hidden = i.get("hidden")
            except AttributeError:
                hidden = ""

            try:
                extension = f'{i.get("extension")}'
            except AttributeError:
                extension = ""

            try:
                image = Image.objects.get(
                    shoper_gfx_id=shoper_gfx_id,
                )
                image.shoper_gfx_id = shoper_gfx_id
                image.shoper_product_id = shoper_product_id
                image.shoper_main = shoper_main
                image.shoper_title_pl = shoper_title_pl
                image.shoper_title_en = shoper_title_en
                image.shoper_title_de = shoper_title_de
                image.shoper_title_fr = shoper_title_fr
                image.order = order
                image.shoper_link_pl = shoper_link_pl
                image.shoper_link_en = shoper_link_en
                image.shoper_link_de = shoper_link_de
                image.shoper_link_fr = shoper_link_fr
                image.shoper_unic = shoper_unic
                image.hidden = hidden
                image.extension = extension
                image.save()
                print("UPDATED: ", image)
            except Image.DoesNotExist:

                Image.objects.create(
                    shoper_gfx_id=shoper_gfx_id,
                    shoper_product_id=shoper_product_id,
                    shoper_main=shoper_main,
                    shoper_title_pl=shoper_title_pl,
                    shoper_title_en=shoper_title_en,
                    shoper_title_de=shoper_title_de,
                    shoper_title_fr=shoper_title_fr,
                    order=order,
                    shoper_link_pl=shoper_link_pl,
                    shoper_link_en=shoper_link_en,
                    shoper_link_de=shoper_link_de,
                    shoper_link_fr=shoper_link_fr,
                    shoper_unic=shoper_unic,
                    hidden=hidden,
                    extension=extension,
                )
                print("CREATED: ", Image)
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
                shoper_description_pl = (
                    i.get("translations").get("pl_PL").get("description")
                )
            except AttributeError:
                shoper_description_pl = ""

            try:
                shoper_description_en = (
                    i.get("translations").get("en_GB").get("description")
                )
            except AttributeError:
                shoper_description_en = ""

            try:
                shoper_description_fr = (
                    i.get("translations").get("fr_FR").get("description")
                )
            except AttributeError:
                shoper_description_fr = ""

            try:
                shoper_description_de = (
                    i.get("translations").get("de_DE").get("description")
                )
            except AttributeError:
                shoper_description_de = ""

            vendor_brand = SHOPER_STORE[0:-3].capitalize()
            shoper_id = i.get("product_id")

            try:
                shoper_ean = i.get("ean")
            except AttributeError:
                shoper_ean = ""

            shoper_sku = i.get("code")

            try:
                shoper_weight = i.get("vol_weight")
            except AttributeError:
                shoper_weight = ""

            is_active_shoper = i.get("stock").get("active")  # dunno if this is right
            created_shoper = i.get("add_date")

            try:
                updated_shoper = i.get("edit_date")
            except AttributeError:
                updated_shoper = ""

            try:
                is_on_shoper = f'{True if i.get("add_date") else ""}'
            except AttributeError:
                is_on_shoper = ""

            try:
                shoper_price = i.get("stock").get("price")
            except AttributeError:
                shoper_price = ""

            try:
                shoper_gauge_id = i.get("gauge_id")
            except:
                shoper_gauge_id = ""

            try:
                product = Product.objects.get(
                    shoper_sku=shoper_sku,
                )
                product.shoper_title_pl = shoper_title_pl
                product.shoper_title_en = shoper_title_en
                product.shoper_title_de = shoper_title_de
                product.shoper_title_fr = shoper_title_fr
                product.shoper_description_pl = shoper_description_pl
                product.shoper_description_en = shoper_description_en
                product.shoper_description_fr = shoper_description_fr
                product.shoper_description_de = shoper_description_de
                product.vendor_brand = vendor_brand
                product.shoper_id = shoper_id
                product.shoper_ean = shoper_ean
                product.shoper_sku = shoper_sku
                product.shoper_weight = shoper_weight
                product.is_active_shoper = is_active_shoper
                product.created_shoper = created_shoper
                product.updated_shoper = updated_shoper
                product.shoper_price = shoper_price
                product.shoper_gauge_id = shoper_gauge_id
                product.is_on_shoper = is_on_shoper
                product.save()
                print("UPDATED: ", product)
            except Product.DoesNotExist:
                Product.objects.create(
                    shoper_title_pl=shoper_title_pl,
                    shoper_title_en=shoper_title_en,
                    shoper_title_de=shoper_title_de,
                    shoper_title_fr=shoper_title_fr,
                    shoper_description_pl=shoper_description_pl,
                    shoper_description_en=shoper_description_en,
                    shoper_description_fr=shoper_description_fr,
                    shoper_description_de=shoper_description_de,
                    vendor_brand=vendor_brand,
                    shoper_id=shoper_id,
                    shoper_ean=shoper_ean,
                    shoper_sku=shoper_sku,
                    shoper_weight=shoper_weight,
                    is_active_shoper=is_active_shoper,
                    created_shoper=created_shoper,
                    updated_shoper=updated_shoper,
                    shoper_price=shoper_price,
                    shoper_gauge_id=shoper_gauge_id,
                    is_on_shoper=is_on_shoper,
                )
                print("CREATED: ", Product)

            time.sleep(1)

    return


def clear_database():
    """..."""

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
