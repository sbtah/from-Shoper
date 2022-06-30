from categories.models import Category
from django.core.management.base import BaseCommand
from external.get_categories import get_all_categories_data


def fetch_all_categories():

    get_all_categories_data()


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database update started, Category objects count: {Category.objects.all().count()}"
            )
        )
        print(fetch_all_categories())
        self.stdout.write(self.style.SUCCESS("Database available!"))
