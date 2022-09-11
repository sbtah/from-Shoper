"""
Prototype so far...
Command that will go through all products or images and set alt('name') according with logic.

"""
import os
from images.models import Image
from products.models import Product
from django.core.management.base import BaseCommand
from apiclient.helpers.logging import logging


def fix_alt_texts():
    """"""
    print(os.getcwd())
    ## Somehow works...
    # all_products = Product.objects.filter(shoper_id=122)
    # # all_products = Product.objects.all()
    # for product in all_products:
    #     print("======================================================")
    #     print(product)
    #     images = product.image_set.all()
    #     for img in images:
    #         print(img.shoper_gfx_id)
    #         image_translations = img.imagetranslation_set.all()
    #         for trans in image_translations:
    #             print(f"Image translation parrent product ID: {trans.related_gfx_id}")
    #             print(f"Image translation locale: {trans.locale}")
    #             print(f"CURRENT ALT: {trans.name}")
    #             product_trans = product.producttranslation_set.get(locale=trans.locale)
    #             if product_trans.active:
    #                 print(f"Is Product translation active : {product_trans.active}")
    #                 print(f"TRANSLATION FOR LOCALE: {product_trans.locale}")
    #                 print(f"ALT TO SET:{product_trans.name}")
    #                 print("---------------------------------------------")
    #             else:
    #                 print("This translation is inactive od product")
    #                 print("---------------------------------------------")


class Command(BaseCommand):
    """Main class for command object that imports images from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(self.style.SUCCESS(f"Starting alt fixing.."))
        fix_alt_texts()
        self.stdout.write(self.style.SUCCESS(f"Alt tag fixing process finished."))
