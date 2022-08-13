import pandas as pd
from django.core.management.base import BaseCommand

# When testing as a script there is no access to database so any database objects have to be commented.
from products.models import Product


CSV_PATH = "Images.csv"


df = pd.read_csv(CSV_PATH, sep=";")
# for row in df.itertuples():
#     print(row)


def load_images_links(data_frame):
    """Load images links from CSV file, to Product class"""

    for row in data_frame.itertuples():
        try:
            # # print(type(row.Images_3))
            # print(f"{'' if row.Images_1 == float else row.Images_1}")
            # print(f"{'' if row.Images_2 == float else row.Images_2}")
            # print(f"{'' if row.Images_3 == 'nan' else row.Images_3}")
            # print(f"{'' if row.Images_4 == 'nan' else row.Images_4}")
            # print(f"{'' if row.Images_5 == 'nan' else row.Images_5}")
            # print(f"{'' if row.Images_6 == 'nan' else row.Images_6}")
            # print(f"{'' if row.Images_7 == 'nan' else row.Images_7}")
            # print(f"{'' if row.Images_8 == 'nan' else row.Images_8}")
            # print(f"{'' if row.Images_9 == 'nan' else row.Images_9}")
            # print(f"{'' if row.Images_10 == 'nan' else row.Images_10}")
            # print(f"{'' if row.Images_11 == 'nan' else row.Images_11}")
            product = Product.objects.get(shoper_sku=row.product_code)
            product.shoper_url_image_1 = row.Images_1
            product.shoper_url_image_2 = row.Images_2
            product.shoper_url_image_3 = row.Images_3
            product.shoper_url_image_4 = row.Images_4
            product.shoper_url_image_5 = row.Images_5
            product.shoper_url_image_6 = row.Images_6
            product.shoper_url_image_7 = row.Images_7
            product.shoper_url_image_8 = row.Images_8
            product.shoper_url_image_9 = row.Images_9
            product.shoper_url_image_10 = row.Images_10
            product.shoper_url_image_11 = row.Images_11
            print(f"{product.shoper_id} has been saved with new Images.")
            product.save()

        except Product.DoesNotExist as e:
            continue


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        load_images_links(df)
