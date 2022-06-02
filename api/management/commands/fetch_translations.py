from django.core.management.base import BaseCommand
from translations.models import ProductTranslation
from external.get_translations import (
    get_all_translations_tags_for_product,
    get_single_product_translation_for_language,
)
from external.get_products import get_list_of_all_shoper_product_ids


def get_all_product_translations_from_shoper_api():

    list_of_product_ids = get_list_of_all_shoper_product_ids()

    for id in list_of_product_ids:
        print(id)
        translation_tags = get_all_translations_tags_for_product(id)
        for tag in translation_tags:
            print(tag)
            translation = get_single_product_translation_for_language(id, tag)
            print(translation)
            # try:
            #     ProductTranslation.objects.get(
            #         shoper_translation_id=translation["translation_id"]
            #     )
            # except ProductTranslation.DoesNotExist:
            #     continue


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(self.style.SUCCESS(f":Starting translations import. "))
        get_all_product_translations_from_shoper_api()

        self.stdout.write(self.style.SUCCESS("Translations available!"))
