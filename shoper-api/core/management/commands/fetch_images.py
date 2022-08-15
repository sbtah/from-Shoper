from images.models import Image
from images.builders import update_or_create_image
from translations.builders import update_or_create_image_translation
from django.core.management.base import BaseCommand
from apiclient.images.get_medium import get_all_images_data
from apiclient.images.get_advanced import (
    from_response_image,
    from_response_translations_for_image,
)
from apiclient.helpers.logging import logging


def fetch_images():
    """Copy all images from SHOPER Api and saves them as Image objects in DB."""

    images = get_all_images_data()
    for img in images:

        logging.info("=" * 78)
        logging.info(f'PROCESSING: Image id: {img["gfx_id"]}')
        image_data = from_response_image(
            response=img,
        )
        image = update_or_create_image(
            shoper_gfx_id=image_data["shoper_gfx_id"],
            shoper_product_id=image_data["shoper_product_id"],
            shoper_main=image_data["shoper_main"],
            shoper_order=image_data["shoper_order"],
            shoper_image_name=image_data["shoper_image_name"],
            shoper_unic=image_data["shoper_unic"],
            shoper_hidden=image_data["shoper_hidden"],
            shoper_extension=image_data["shoper_extension"],
        )
        translations = from_response_translations_for_image(
            response=image_data["shoper_image_translations"]
        )
        for trans in translations:
            translation = update_or_create_image_translation(
                locale=trans["locale"],
                shoper_translation_id=trans["shoper_translation_id"],
                related_gfx_id=trans["related_gfx_id"],
                name=trans["name"],
                lang_id=trans["lang_id"],
            )


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
