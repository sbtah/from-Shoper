import requests
import time
import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from images.models import Image


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

            image = Image.objects.update_or_create(
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
            image.save()
            time.sleep(1)
            print(f"Image for Product ID:{image.shoper_product_id} Downloaded")

    return


def clear_data():
    Image.objects.all().delete()


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        clear_data()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Image objects count: {Image.objects.all().count()}"
            )
        )
        copy_all_product_images_from_shoper_api()
        self.stdout.write(self.style.SUCCESS("Database available!"))
