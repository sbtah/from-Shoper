from categories.models import Category
from apiclient.helpers.logging import logging


def update_or_create_category(
    shoper_id,
    shoper_category_is_root,
    shoper_order,
):
    """Create or Update an instance of Category object from items provided from API call to Shoper API."""

    try:
        category = Category.objects.get(shoper_id=shoper_id)
        if (
            (str(shoper_id) != str(category.shoper_id))
            or (str(shoper_category_is_root) != str(category.shoper_category_is_root))
            or (str(shoper_order) != str(category.shoper_order))
        ):
            category.shoper_id = shoper_id

            category.shoper_category_is_root = shoper_category_is_root
            category.shoper_order = shoper_order
            category.save()
            logging.info(f"!! UPDATE Category: {category.shoper_id}")
        else:
            logging.info(f"NO UPDATES for Category: {category.shoper_id}")
    except Category.DoesNotExist:
        category = Category.objects.create(
            shoper_id=shoper_id,
            shoper_category_is_root=shoper_category_is_root,
            shoper_order=shoper_order,
        )
        logging.info(f"!! CREATE Category: {category.shoper_id}")

    return category
