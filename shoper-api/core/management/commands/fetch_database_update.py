from django.core.management.base import BaseCommand
from images.models import Image
from products.models import Product
from api.management.commands.fetch_categories import fetch_categories
from api.management.commands.fetch_products import fetch_products
from api.management.commands.fetch_images import (
    fetch_images,
)


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
        fetch_categories()
        fetch_products()
        fetch_images()

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Database available!
        Number of Products: {Product.objects.all().count()}
        Number of Images: {Image.objects.all().count()}
        """
            )
        )
