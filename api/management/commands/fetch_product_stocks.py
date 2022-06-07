import requests
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from products.models import Product
from stocks.models import Stock
from translations.models import ProductTranslation
from external.get_token import SHOPER_STORE, TOKEN
from external.get_products import (
    get_number_of_product_pages,
)

# TODO
# THIS Command is unfinished.

# Get all ID numbers of products from SHOPER Api.
def copy_all_stocks_from_shoper_api():
    """Copy all products from SHOPER Api and saves them as Product objects in DB."""

    number_of_product_pages = get_number_of_product_pages()

    for x in range(1, number_of_product_pages + 1):
        data = {"page": f"{x}"}
        url = f"https://{SHOPER_STORE}/webapi/rest/products"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        response = requests.get(url, headers=headers, params=data)
        res = response.json()
        items = res.get("list")

        for i in items:
            """
            Loops over part of response with all products.
            """

            print("===STOCK===")
            # Stock data from response.
            shoper_stock_id = i.get("stock").get("stock_id")
            shoper_stock_product_id = i.get("stock").get("product_id")
            shoper_stock_extended = i.get("stock").get("extended")
            shoper_stock_price = i.get("stock").get("price")
            shoper_stock_active = i.get("stock").get("active")
            shoper_stock_default = i.get("stock").get("default")
            shoper_stock_value = i.get("stock").get("stock")
            shoper_stock_warn_level = i.get("stock").get("warn_level")
            shoper_stock_sold = i.get("stock").get("sold")
            shoper_stock_code = i.get("stock").get("code")
            shoper_stock_ean = i.get("stock").get("ean")
            shoper_stock_weight = i.get("stock").get("weight")
            shoper_stock_weight_type = i.get("stock").get("weight_type")
            shoper_stock_availability_id = i.get("stock").get("availability_id")
            shoper_stock_delivery_id = i.get("stock").get("delivery_id")
            shoper_stock_gfx_id = i.get("stock").get("gfx_id")
            shoper_stock_package = i.get("stock").get("package")
            shoper_stock_price_wholesale = i.get("stock").get("price_wholesale")
            shoper_stock_price_special = i.get("stock").get("price_special")
            shoper_stock_calculation_unit_id = i.get("stock").get("calculation_unit_id")
            shoper_stock_calculation_unit_ratio = i.get("stock").get(
                "calculation_unit_ratio"
            )
            """===STOCK==="""
            """
            Tries to fetch Product's Stock object from DB and update it.
            Creates new object if fails.
            """
            try:
                stock = Stock.objects.get(shoper_stock_id=shoper_stock_id)
                if (
                    (str(stock.shoper_stock_id) != str(shoper_stock_id))
                    or (
                        str(stock.shoper_stock_product_id)
                        != str(shoper_stock_product_id)
                    )
                    or (str(stock.shoper_stock_extended) != str(shoper_stock_extended))
                    or (str(stock.shoper_stock_price) != str(shoper_stock_price))
                    or (str(stock.shoper_stock_active) != str(shoper_stock_active))
                    or (str(stock.shoper_stock_default) != str(shoper_stock_default))
                    or (str(stock.shoper_stock_value) != str(shoper_stock_value))
                    or (
                        str(stock.shoper_stock_warn_level)
                        != str(shoper_stock_warn_level)
                    )
                    or (str(stock.shoper_stock_sold) != str(shoper_stock_sold))
                    or (str(stock.shoper_stock_code) != str(shoper_stock_code))
                    or (str(stock.shoper_stock_ean) != str(shoper_stock_ean))
                    or (str(stock.shoper_stock_weight) != str(shoper_stock_weight))
                    or (
                        str(stock.shoper_stock_weight_type)
                        != str(shoper_stock_weight_type)
                    )
                    or (
                        str(stock.shoper_stock_availability_id)
                        != str(shoper_stock_availability_id)
                    )
                    or (
                        str(stock.shoper_stock_delivery_id)
                        != str(shoper_stock_delivery_id)
                    )
                    or (str(stock.shoper_stock_gfx_id) != str(shoper_stock_gfx_id))
                    or (str(stock.shoper_stock_package) != str(shoper_stock_package))
                    or (
                        str(stock.shoper_stock_price_wholesale)
                        != str(shoper_stock_price_wholesale)
                    )
                    or (
                        str(stock.shoper_stock_price_special)
                        != str(shoper_stock_price_special)
                    )
                    or (
                        str(stock.shoper_stock_calculation_unit_id)
                        != str(shoper_stock_calculation_unit_id)
                    )
                    or (
                        str(stock.shoper_stock_calculation_unit_ratio)
                        != str(shoper_stock_calculation_unit_ratio)
                    )
                ):
                    stock.shoper_stock_id = shoper_stock_id
                    stock.shoper_stock_product_id = shoper_stock_product_id
                    stock.shoper_stock_extended = shoper_stock_extended
                    stock.shoper_stock_price = shoper_stock_price
                    stock.shoper_stock_active = shoper_stock_active
                    stock.shoper_stock_default = shoper_stock_default
                    stock.shoper_stock_value = shoper_stock_value
                    stock.shoper_stock_warn_level = shoper_stock_warn_level
                    stock.shoper_stock_sold = shoper_stock_sold
                    stock.shoper_stock_code = shoper_stock_code
                    stock.shoper_stock_ean = shoper_stock_ean
                    stock.shoper_stock_weight = shoper_stock_weight
                    stock.shoper_stock_weight_type = shoper_stock_weight_type
                    stock.shoper_stock_availability_id = shoper_stock_availability_id
                    stock.shoper_stock_delivery_id = shoper_stock_delivery_id
                    stock.shoper_stock_gfx_id = shoper_stock_gfx_id
                    stock.shoper_stock_package = shoper_stock_package
                    stock.shoper_stock_price_wholesale = shoper_stock_price_wholesale
                    stock.shoper_stock_price_special = shoper_stock_price_special
                    stock.shoper_stock_calculation_unit_id = (
                        shoper_stock_calculation_unit_id
                    )
                    stock.shoper_stock_calculation_unit_ratio = (
                        shoper_stock_calculation_unit_ratio
                    )
                    parrent_product = Product.objects.get(
                        shoper_id=stock.shoper_stock_product_id
                    )
                    parrent_product.stock_set.add(stock)
                    stock.save()
                    print(f"Stock: {stock.shoper_stock_id} Updated")
                else:
                    parrent_product = Product.objects.get(
                        shoper_id=stock.shoper_stock_product_id
                    )
                    parrent_product.stock_set.add(stock)
                    print(f"No updates Stock: {stock.shoper_stock_id}")
            except Stock.DoesNotExist:
                stock = Stock.objects.create(
                    shoper_stock_id=shoper_stock_id,
                    shoper_stock_product_id=shoper_stock_product_id,
                    shoper_stock_extended=shoper_stock_extended,
                    shoper_stock_price=shoper_stock_price,
                    shoper_stock_active=shoper_stock_active,
                    shoper_stock_default=shoper_stock_default,
                    shoper_stock_value=shoper_stock_value,
                    shoper_stock_warn_level=shoper_stock_warn_level,
                    shoper_stock_sold=shoper_stock_sold,
                    shoper_stock_code=shoper_stock_code,
                    shoper_stock_ean=shoper_stock_ean,
                    shoper_stock_weight=shoper_stock_weight,
                    shoper_stock_weight_type=shoper_stock_weight_type,
                    shoper_stock_availability_id=shoper_stock_availability_id,
                    shoper_stock_delivery_id=shoper_stock_delivery_id,
                    shoper_stock_gfx_id=shoper_stock_gfx_id,
                    shoper_stock_package=shoper_stock_package,
                    shoper_stock_price_wholesale=shoper_stock_price_wholesale,
                    shoper_stock_price_special=shoper_stock_price_special,
                    shoper_stock_calculation_unit_id=shoper_stock_calculation_unit_id,
                    shoper_stock_calculation_unit_ratio=shoper_stock_calculation_unit_ratio,
                )
                parrent_product = Product.objects.get(
                    shoper_id=stock.shoper_stock_product_id
                )
                parrent_product.stock_set.add(stock)
                print(f"Stock : {stock.shoper_stock_id} Created")


class Command(BaseCommand):
    """Main class for command object that imports products from shoper."""

    def handle(self, *args, **options):
        """Custom handle method."""

        self.stdout.write(
            self.style.SUCCESS(
                f"Database cleared Product objects count: {Product.objects.all().count()}"
            )
        )
        copy_all_stocks_from_shoper_api()
        self.stdout.write(self.style.SUCCESS("Database available!"))
