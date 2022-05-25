import pandas as pd
from django.core.management.base import BaseCommand

# When testing as a script there is no access to database so any database objects have to be commented.
from products.models import Product


CSV_PATH = "Images-GB.csv"


df = pd.read_csv(CSV_PATH, sep=";")
# for row in df.itertuples():
#     print(row)


def load_images_links(data_frame):
    """Load images links from CSV file, to Product class"""

    for row in data_frame.itertuples():
        print(row.product_code)
        product = Product.objects.get(shoper_sku=row.product_code)

        print(product)


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        load_images_links(df)
