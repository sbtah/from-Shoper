import time
from images.models import Image
from products.models import Product
from django.core.management.base import BaseCommand
from core.management.commands.fetch_categories import fetch_categories_v2
from core.management.commands.fetch_products import fetch_products_v2
from core.management.commands.fetch_images import (
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
        start_time_all = time.perf_counter()
        start_categories = time.perf_counter()
        fetch_categories_v2()
        end_categories = time.perf_counter()
        start_products = time.perf_counter()
        fetch_products_v2()
        end_products = time.perf_counter()
        start_images = time.perf_counter()
        fetch_images()
        end_images = time.perf_counter()

        self.stdout.write(
            self.style.SUCCESS(
                f"""
        Database available!
        Number of Products: {Product.objects.all().count()}
        Number of Images: {Image.objects.all().count()}
        Seconds for Categories: {end_categories - start_categories}
        Seconds for Products: {end_products - start_products}
        Seconds for Images: {end_images - start_images}
        Seconds for Entire DB: {end_images - start_time_all}
        """
            )
        )
