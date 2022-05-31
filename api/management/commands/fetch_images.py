import requests
import time
from external.get_token import SHOPER_STORE, TOKEN
from django.core.management.base import BaseCommand
from images.models import Image


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

    number_of_images_pages = get_number_of_image_pages()

    for x in range(1, number_of_images_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/product-images"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")
        # tags = (tag for tag in res.get("translations"))

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


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Starting update. Number of Images: {Image.objects.all().count()}"
            )
        )
        copy_all_product_images_from_shoper_api()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database available, number of Images after update: {Image.objects.all().count()}"
            )
        )
