import time
import requests
from external.get_token import SHOPER_STORE, TOKEN
from django.core.management.base import BaseCommand
from translations.models import ProductTranslation
from external.get_products import (
    get_number_of_product_pages,
)


# TODO
# THIS COMMAND IS UNFINISHED
def get_all_product_translations_from_shoper_api():
    """Copy all product' translations from SHOPER Api and saves them as ProductTranslation objects in DB."""

    count_id = []

    number_of_product_pages = get_number_of_product_pages()

    for x in range(1, number_of_product_pages + 1):

        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        time.sleep(0.5)
        res = response.json()
        items = res.get("list")

        for i in items:

            shoper_product_id = i.get("product_id")
            count_id.append(shoper_product_id)
            print("PRODUCT ID: ", shoper_product_id)

            for tag in i.get("translations"):

                """Create Products Translation for each language Tag on current product."""

                # Get Variables from each of translations that Product currently have.
                locale = tag
                shoper_translation_id = (
                    i.get("translations").get(f"{locale}").get("translation_id")
                )
                related_product_id = (
                    i.get("translations").get(f"{locale}").get("product_id")
                )
                name = i.get("translations").get(f"{locale}").get("name")
                short_description = (
                    i.get("translations").get(f"{locale}").get("short_description")
                )
                description = i.get("translations").get(f"{locale}").get("description")
                active = i.get("translations").get(f"{locale}").get("active")
                is_default = i.get("translations").get(f"{locale}").get("isdefault")
                lang_id = i.get("translations").get(f"{locale}").get("lang_id")
                seo_title = i.get("translations").get(f"{locale}").get("seo_title")
                seo_description = (
                    i.get("translations").get(f"{locale}").get("seo_description")
                )
                seo_keywords = (
                    i.get("translations").get(f"{locale}").get("seo_keywords")
                )
                seo_url = i.get("translations").get(f"{locale}").get("seo_url")
                permalink = i.get("translations").get(f"{locale}").get("permalink")
                order = i.get("translations").get(f"{locale}").get("order")
                main_page = i.get("translations").get(f"{locale}").get("main_page")
                main_page_order = (
                    i.get("translations").get(f"{locale}").get("main_page_order")
                )
                """
                Tries to fetch existing Product Translation from DB and update it.
                Creates new object if fails.
                """
                print(locale)
                print(shoper_translation_id)
                try:
                    translation = ProductTranslation.objects.get(
                        shoper_translation_id=shoper_translation_id
                    )
                    """
                    Checks is data translation data in DB is not different from response.
                    If there is a difference on one of the fields, model is updated.
                    """
                    if (
                        (str(translation.locale) != str(locale))
                        or (
                            str(translation.shoper_translation_id)
                            != str(shoper_translation_id)
                        )
                        or (
                            str(translation.related_product_id)
                            != str(related_product_id)
                        )
                        or (str(translation.name) != str(name))
                        or (
                            str(translation.short_description) != str(short_description)
                        )
                        or (str(translation.description) != str(description))
                        or (str(translation.active) != str(active))
                        or (str(translation.is_default) != str(is_default))
                        or (str(translation.lang_id) != str(lang_id))
                        or (str(translation.seo_title) != str(seo_title))
                        or (str(translation.seo_description) != str(seo_description))
                        or (str(translation.seo_keywords) != str(seo_keywords))
                        or (str(translation.seo_url) != str(seo_url))
                        or (str(translation.permalink) != str(permalink))
                        or (str(translation.order) != str(order))
                        or (str(translation.main_page) != str(main_page))
                        or (str(translation.main_page_order) != str(main_page_order))
                    ):
                        translation.locale = locale
                        translation.shoper_translation_id = shoper_translation_id
                        translation.related_product_id = related_product_id
                        translation.name = name
                        translation.short_description = short_description
                        translation.description = description
                        translation.active = active
                        translation.is_default = is_default
                        translation.lang_id = lang_id
                        translation.seo_title = seo_title
                        translation.seo_description = seo_description
                        translation.seo_keywords = seo_keywords
                        translation.seo_url = seo_url
                        translation.permalink = permalink
                        translation.order = order
                        translation.main_page = main_page
                        translation.description = description
                        translation.main_page_order = main_page_order
                        translation.save()
                        print(f"Translation: {translation.related_product_id} Updated")
                    else:
                        print(
                            f"No updates for Translation: {translation.related_product_id}"
                        )
                except ProductTranslation.DoesNotExist:
                    print()
                    translation = ProductTranslation.objects.create(
                        locale=locale,
                        shoper_translation_id=shoper_translation_id,
                        related_product_id=related_product_id,
                        name=name,
                        short_description=short_description,
                        description=description,
                        active=active,
                        is_default=is_default,
                        lang_id=lang_id,
                        seo_title=seo_title,
                        seo_description=seo_description,
                        seo_keywords=seo_keywords,
                        seo_url=seo_url,
                        permalink=permalink,
                        order=order,
                        main_page=main_page,
                        main_page_order=main_page_order,
                    )
                    print(f"Translation created {translation.shoper_translation_id}")
    print(count_id)
    print(len(count_id))


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(self.style.SUCCESS(f":Starting translations import. "))
        get_all_product_translations_from_shoper_api()

        self.stdout.write(self.style.SUCCESS("Translations available!"))
