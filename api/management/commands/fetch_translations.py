from django.core.management.base import BaseCommand
from external.get_translations import (
    get_all_translations_tags_for_product,
    get_single_product_translation_for_language,
)
from external.get_products import get_number_of_product_pages


def get_all_product_translations_from_shoper_api():

    list_of_shoper_ids = get_number_of_product_pages()

    for id in list_of_shoper_ids:
        for tag in get_all_translations_tags_for_product(id):
            print(tag)
            body = get_single_product_translation_for_language(id, tag)
            print(body["name"])


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(self.style.SUCCESS(f":Starting translations import. "))
        get_all_product_translations_from_shoper_api()

        self.stdout.write(self.style.SUCCESS("Translations available!"))
