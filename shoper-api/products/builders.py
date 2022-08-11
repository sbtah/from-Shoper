from datetime import datetime
from products.models import Product
from categories.models import Category


def update_or_create_product(
    shoper_id,
    shoper_type,
    shoper_producer_id,
    shoper_group_id,
    shoper_tax_id,
    shoper_main_category_id,
    shoper_all_categories_ids,
    shoper_unit_id,
    created_shoper,
    updated_shoper,
    shoper_other_price,
    shoper_promo_price,
    shoper_sku,
    shoper_ean,
    shoper_pkwiu,
    shoper_is_product_of_day,
    shoper_bestseller_tag,
    shoper_new_product_tag,
    shoper_vol_weight,
    shoper_gauge_id,
    shoper_currency_id,
    shoper_promo_id,
    shoper_promo_start,
    shoper_promo_ends,
    shoper_discount_value,
):
    """Create or Update an instance of Product object from items provided from API call to Shoper API."""
    try:
        product = Product.objects.get(
            shoper_sku=shoper_sku,
        )
        if datetime.strptime(updated_shoper, "%Y-%m-%d %H:%M:%S") > datetime.strptime(
            product.updated_shoper, "%Y-%m-%d %H:%M:%S"
        ):
            # Shoper Main Data
            product.shoper_id = shoper_id
            product.shoper_type = shoper_type
            product.shoper_producer_id = shoper_producer_id
            product.shoper_group_id = shoper_group_id
            product.shoper_tax_id = shoper_tax_id
            product.shoper_main_category_id = shoper_main_category_id
            product.shoper_all_categories_ids = shoper_all_categories_ids
            product.shoper_unit_id = shoper_unit_id
            product.created_shoper = created_shoper
            product.updated_shoper = updated_shoper
            product.shoper_other_price = shoper_other_price
            product.shoper_promo_price = shoper_promo_price
            product.shoper_sku = shoper_sku
            product.shoper_ean = shoper_ean
            product.shoper_pkwiu = shoper_pkwiu
            product.shoper_is_product_of_day = shoper_is_product_of_day
            product.shoper_bestseller_tag = shoper_bestseller_tag
            product.shoper_new_product_tag = shoper_new_product_tag
            product.shoper_vol_weight = shoper_vol_weight
            product.shoper_gauge_id = shoper_gauge_id
            product.shoper_currency_id = shoper_currency_id
            # Shoper Special Offer.
            product.shoper_promo_id = shoper_promo_id
            product.shoper_promo_start = shoper_promo_start
            product.shoper_promo_ends = shoper_promo_ends
            product.shoper_discount_value = shoper_discount_value
            product.save()

            parrent_categories = Category.objects.filter(
                shoper_id__in=shoper_all_categories_ids
            )
            for category in parrent_categories:
                category.shoper_products.add(product)
            print(f"!! Product updated: {product}")
        else:
            print(f"No update for Product: {product}")
            parrent_categories = Category.objects.filter(
                shoper_id__in=shoper_all_categories_ids
            )
            for category in parrent_categories:
                category.shoper_products.add(product)
    except Product.DoesNotExist:
        product = Product.objects.create(
            shoper_id=shoper_id,
            shoper_type=shoper_type,
            shoper_producer_id=shoper_producer_id,
            shoper_group_id=shoper_group_id,
            shoper_tax_id=shoper_tax_id,
            shoper_main_category_id=shoper_main_category_id,
            shoper_all_categories_ids=shoper_all_categories_ids,
            shoper_unit_id=shoper_unit_id,
            created_shoper=created_shoper,
            updated_shoper=updated_shoper,
            shoper_other_price=shoper_other_price,
            shoper_promo_price=shoper_promo_price,
            shoper_sku=shoper_sku,
            shoper_ean=shoper_ean,
            shoper_pkwiu=shoper_pkwiu,
            shoper_is_product_of_day=shoper_is_product_of_day,
            shoper_bestseller_tag=shoper_bestseller_tag,
            shoper_new_product_tag=shoper_new_product_tag,
            shoper_vol_weight=shoper_vol_weight,
            shoper_gauge_id=shoper_gauge_id,
            shoper_currency_id=shoper_currency_id,
            shoper_promo_id=shoper_promo_id,
            shoper_promo_start=shoper_promo_start,
            shoper_promo_ends=shoper_promo_ends,
            shoper_discount_value=shoper_discount_value,
        )
        parrent_categories = Category.objects.filter(
            shoper_id__in=shoper_all_categories_ids
        )
        for category in parrent_categories:
            category.shoper_products.add(product)
        print(f"!! Product created: {product}")
    return product
