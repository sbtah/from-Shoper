from categories.models import Category
from categories.builders import update_or_create_category
from translations.builders import update_or_create_category_translation
from django.core.management.base import BaseCommand
from external.get_categories import get_all_categories_data


def fetch_categories():
    """This function creates categories with related translation from a GET response to Shoper's API"""

    for i in get_all_categories_data():
        category_id = i.get("category_id")
        root = i.get("root")
        order = i.get("order")
        update_or_create_category(
            shoper_id=category_id,
            shoper_category_is_root=root,
            shoper_order=order,
        )
        for tag in i.get("translations"):
            locale = tag
            shoper_translation_id = i.get("translations").get(tag).get("trans_id")
            related_category_id = i.get("translations").get(tag).get("category_id")
            name = i.get("translations").get(tag).get("name")
            description = i.get("translations").get(tag).get("description")
            description_bottom = (
                i.get("translations").get(tag).get("description_bottom")
            )
            seo_title = i.get("translations").get(tag).get("seo_title")
            seo_description = i.get("translations").get(tag).get("seo_description")
            seo_keywords = i.get("translations").get(tag).get("seo_keywords")
            seo_url = i.get("translations").get(tag).get("seo_url")
            permalink = i.get("translations").get(tag).get("permalink")
            active = i.get("translations").get(tag).get("active")
            is_default = i.get("translations").get(tag).get("is_default")
            lang_id = i.get("translations").get(tag).get("lang_id")
            items = i.get("translations").get(tag).get("items")
            update_or_create_category_translation(
                locale=locale,
                shoper_translation_id=shoper_translation_id,
                related_category_id=related_category_id,
                name=name,
                description=description,
                description_bottom=description_bottom,
                seo_title=seo_title,
                seo_description=seo_description,
                seo_keywords=seo_keywords,
                seo_url=seo_url,
                permalink=permalink,
                active=active,
                is_default=is_default,
                lang_id=lang_id,
                items=items,
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
        fetch_categories()
        self.stdout.write(
            self.style.SUCCESS(
                f"Database available, Category objects count: {Category.objects.all().count()}"
            )
        )
