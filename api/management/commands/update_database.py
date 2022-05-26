import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from images.models import Image
from products.models import Product
from commands.import_products import copy_all_products_from_shoper_api
from commands.import_images import copy_all_product_images_from_shoper_api


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
