from categories.models import Category
from categories.builders import update_or_create_category
from translations.builders import update_or_create_category_translation
from django.core.management.base import BaseCommand
from apiclient.categories.get_medium import get_all_categories_data
from apiclient.categories.get_advanced import (
    from_response_category,
    from_response_translations_for_category,
)
from apiclient.helpers.logging import logging


def fetch_categories_v2():
    """This function creates categories with related translation from a GET response to Shoper's API"""

    category_data = get_all_categories_data()
    for cat in category_data:

        logging.info("=" * 78)
        logging.info(f'PROCESSING: Category id: {cat["category_id"]}')
        category_data = from_response_category(
            response=cat,
        )
        category = update_or_create_category(
            shoper_id=category_data["category_id"],
            shoper_category_is_root=category_data["root"],
            shoper_order=category_data["order"],
        )
        translations = from_response_translations_for_category(
            response=category_data["category_translations"],
        )
        for trans in translations:
            translation = update_or_create_category_translation(
                locale=trans["locale"],
                shoper_translation_id=trans["shoper_translation_id"],
                related_category_id=trans["related_category_id"],
                name=trans["category_name"],
                description=trans["category_description"],
                description_bottom=trans["category_description_bottom"],
                seo_title=trans["category_seo_title"],
                seo_description=trans["category_seo_description"],
                seo_keywords=trans["category_seo_keywords"],
                seo_url=trans["category_seo_url"],
                permalink=trans["category_permalink"],
                active=trans["category_active"],
                is_default=trans["category_is_default"],
                lang_id=trans["category_lang_id"],
                items=trans["category_items"],
            )


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database update started, Category objects count: {Category.objects.all().count()}"
            )
        )
        # print(get_all_categories_data())
        fetch_categories_v2()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database available, Category objects count: {Category.objects.all().count()}"
            )
        )
