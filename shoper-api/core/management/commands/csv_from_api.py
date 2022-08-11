from django.core.management.base import BaseCommand
from external.get_products import get_list_of_all_shoper_product_ids_for_lang


def generate_product_sku_name_for_lang(language, file_name):

    with open(f"{file_name}.csv", "w") as file:
        file.write(f"product_code;name")

    for id in get_list_of_all_shoper_product_ids_for_lang(lang_code=language[3:]):
        print(id)

    # WORKS AFTER WE HAVE THOSE IN DB!
    # with open(f"{file_name}.csv", "a") as file:
    #     file.write(
    #         f"\n{product.shoper_id};{product.shoper_sku};{product.shoper_category_id};{product.current_link};{product.seo_link}"
    #     )


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "lang_code",
            type=str,
            help="Indicates the language for product range to generate rapport.",
        )
        parser.add_argument(
            "file_name",
            type=str,
            help="Indicates the file name in which raport will be generated.",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        lang = kwargs["lang_code"]
        file = kwargs["file_name"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Generate rapport data.
                """
            )
        )
        generate_product_sku_name_for_lang(lang, file)
        # print(get_list_of_all_shoper_product_ids_for_lang("US"))
        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Process finished
                """
            )
        )
