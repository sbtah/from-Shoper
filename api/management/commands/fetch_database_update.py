from django.core.management.base import BaseCommand
from images.models import Image
from products.models import Product
from api.management.commands.fetch_products import copy_all_products_from_shoper_api
from api.management.commands.fetch_images import (
    copy_all_product_images_from_shoper_api,
)


# def clear_database():
#     """
#     Clears Images and Products from DB.
#     Used for testing.
#     """

#     Image.objects.all().delete()
#     Product.objects.all().delete()


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
        # COPY ALL TRANSLATIONS!
        copy_all_products_from_shoper_api()
        copy_all_product_images_from_shoper_api()

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Database available!
        Number of Products: {Product.objects.all().count()}
        Number of Images: {Image.objects.all().count()}
        """
            )
        )
