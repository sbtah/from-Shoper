from images.models import Image
from images.builders import update_or_create_image
from translations.builders import update_or_create_image_translation
from django.core.management.base import BaseCommand
from external.get_images import get_all_images_data


def fetch_images():
    """Copy all images from SHOPER Api and saves them as Image objects in DB."""

    for i in get_all_images_data():
        """Loops over part of response with all Images."""

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
        except AttributeError:
            shoper_hidden = ""

        try:
            shoper_extension = i.get("extension")
        except AttributeError:
            shoper_extension = ""
        update_or_create_image(
            shoper_gfx_id=shoper_gfx_id,
            shoper_product_id=shoper_product_id,
            shoper_main=shoper_main,
            shoper_order=shoper_order,
            shoper_image_name=shoper_image_name,
            shoper_unic=shoper_unic,
            shoper_hidden=shoper_hidden,
            shoper_extension=shoper_extension,
        )
        for tag in i.get("translations"):
            locale = tag
            shoper_translation_id = (
                i.get("translations").get(locale).get("translation_id")
            )
            related_gfx_id = i.get("translations").get(locale).get("gfx_id")
            name = i.get("translations").get(locale).get("name")
            lang_id = i.get("translations").get(locale).get("lang_id")
            update_or_create_image_translation(
                locale=locale,
                shoper_translation_id=shoper_translation_id,
                related_gfx_id=related_gfx_id,
                name=name,
                lang_id=lang_id,
            )
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
        fetch_images()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database available, Number of Images after update: {Image.objects.all().count()}"
            )
        )
