from django.core.management.base import BaseCommand
from products.models import Product


def generate_simple_product_for_language(language, file_name):

    with open(f"{file_name}.csv", "w") as file:
        file.write(f"product_code;name")
    # filter(field__like='10%8%0%')
    query_set = Product.objects.filter(shoper_sku__endswith=f"{language[3:]}")
    print(f"Number of products: {query_set.count()}")

    for item in query_set:
        if language == "pl_PL":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_pl}")
        elif language == "en_GB":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_gb})")
        elif language == "en_IE":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_eu})")
        elif language == "de_DE":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_de})")
        elif language == "fr_FR":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_fr})")
        elif language == "en_US":
            print(item.shoper_id)
            with open(f"{file_name}.csv", "a") as file:
                file.write(f"\n{item.shoper_sku};{item.shoper_title_us})")


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def add_arguments(self, parser):
        parser.add_argument(
            "language",
            type=str,
            help="Indicates the language TAG for product range to generate rapport.",
        )
        parser.add_argument(
            "file_name",
            type=str,
            help="Indicates the language TAG for product range to generate rapport.",
        )

    def handle(self, *args, **kwargs):
        """Custom handle method."""

        lang = kwargs["language"]
        file = kwargs["file_name"]

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Generate rapport data.
                """
            )
        )
        generate_simple_product_for_language(lang, file)

        self.stdout.write(
            self.style.SUCCESS(
                f"""
                Process finished
                """
            )
        )
