import requests
import time
from images.models import Image
from translations.models import ImageTranslation
from django.core.management.base import BaseCommand
from external.get_token import SHOPER_STORE, TOKEN
from external.get_images import get_number_of_image_pages


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

        for i in items:
            shoper_gfx_id = i.get("gfx_id")
            print(shoper_gfx_id)
            try:
                for tag in i.get("translations"):
                    print(tag)

                    translation = ImageTranslation.objects.update_or_create(
                        locale=tag,
                        shoper_translation_id=i.get("translations")
                        .get(tag)
                        .get("translation_id"),
                        related_gfx_id=i.get("translations").get(tag).get("gfx_id"),
                        name=i.get("translations").get(tag).get("name"),
                        lang_id=i.get("translations").get(tag).get("lang_id"),
                    )
                    print(f"Translation:{translation[0]}")
                    print(f"Created:{translation[1]}")
            except TypeError:
                continue

            try:
                shoper_product_id = i.get("product_id")
            except AttributeError:
                shoper_product_id = ""

            try:
                shoper_main = i.get("main")
            except AttributeError:
                shoper_main = ""

            try:
                shoper_order = i.get("order")
            except AttributeError:
                shoper_order = ""

            try:
                shoper_image_name = i.get("name")
            except AttributeError:
                shoper_image_name = ""

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
                    or (str(image.shoper_order) != str(shoper_order))
                    or (str(image.shoper_image_name) != str(shoper_image_name))
                    or (str(image.shoper_unic) != str(shoper_unic))
                    or (str(image.shoper_hidden) != str(shoper_hidden))
                    or (str(image.shoper_extension) != str(shoper_extension))
                ):
                    image.shoper_gfx_id = shoper_gfx_id
                    image.shoper_product_id = shoper_product_id
                    image.shoper_main = shoper_main
                    image.shoper_order = shoper_order
                    image.shoper_image_name = shoper_image_name
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
                    shoper_order=shoper_order,
                    shoper_image_name=shoper_image_name,
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
