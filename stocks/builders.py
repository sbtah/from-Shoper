from stocks.models import Stock
from products.models import Product


def update_or_create_category_stock(
    shoper_stock_id,
    shoper_stock_product_id,
    shoper_stock_extended,
    shoper_stock_price,
    shoper_stock_active,
    shoper_stock_default,
    shoper_stock_value,
    shoper_stock_warn_level,
    shoper_stock_sold,
    shoper_stock_code,
    shoper_stock_ean,
    shoper_stock_weight,
    shoper_stock_weight_type,
    shoper_stock_availability_id,
    shoper_stock_delivery_id,
    shoper_stock_gfx_id,
    shoper_stock_package,
    shoper_stock_price_wholesale,
    shoper_stock_price_special,
    shoper_stock_calculation_unit_id,
    shoper_stock_calculation_unit_ratio,
):
    """Create or Update an instance of Stock object with data coming from API call to Shoper's store."""
    try:
        stock = Stock.objects.get(shoper_stock_id=shoper_stock_id)
        if (
            (str(stock.shoper_stock_id) != str(shoper_stock_id))
            or (str(stock.shoper_stock_product_id) != str(shoper_stock_product_id))
            or (str(stock.shoper_stock_extended) != str(shoper_stock_extended))
            or (str(stock.shoper_stock_price) != str(shoper_stock_price))
            or (str(stock.shoper_stock_active) != str(shoper_stock_active))
            or (str(stock.shoper_stock_default) != str(shoper_stock_default))
            or (str(stock.shoper_stock_value) != str(shoper_stock_value))
            or (str(stock.shoper_stock_warn_level) != str(shoper_stock_warn_level))
            or (str(stock.shoper_stock_sold) != str(shoper_stock_sold))
            or (str(stock.shoper_stock_code) != str(shoper_stock_code))
            or (str(stock.shoper_stock_ean) != str(shoper_stock_ean))
            or (str(stock.shoper_stock_weight) != str(shoper_stock_weight))
            or (str(stock.shoper_stock_weight_type) != str(shoper_stock_weight_type))
            or (
                str(stock.shoper_stock_availability_id)
                != str(shoper_stock_availability_id)
            )
            or (str(stock.shoper_stock_delivery_id) != str(shoper_stock_delivery_id))
            or (str(stock.shoper_stock_gfx_id) != str(shoper_stock_gfx_id))
            or (str(stock.shoper_stock_package) != str(shoper_stock_package))
            or (
                str(stock.shoper_stock_price_wholesale)
                != str(shoper_stock_price_wholesale)
            )
            or (
                str(stock.shoper_stock_price_special) != str(shoper_stock_price_special)
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
            stock.shoper_stock_calculation_unit_id = shoper_stock_calculation_unit_id
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
        parrent_product = Product.objects.get(shoper_id=stock.shoper_stock_product_id)
        parrent_product.stock_set.add(stock)
        print(f"Stock : {stock.shoper_stock_id} Created")
    return stock
