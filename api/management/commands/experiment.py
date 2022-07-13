from django.core.management.base import BaseCommand
from external.get_products import get_single_product


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(self.style.SUCCESS(f"Test!"))
        data = get_single_product(122)
        print(data.get("stock"))
        # for lang in data.get("translations"):
        #     print(lang)
        self.stdout.write(self.style.SUCCESS("Test Done!"))
