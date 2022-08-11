from categories.models import Category


def update_or_create_category(shoper_id, shoper_category_is_root, shoper_order):
    """Create or Update an instance of Category object from items provided from API call to Shoper API."""

    try:
        category = Category.objects.get(shoper_id=shoper_id)
        if (
            (shoper_id != category.shoper_id)
            or (shoper_category_is_root != category.shoper_category_is_root)
            or (shoper_order != category.shoper_order)
        ):
            category.shoper_id = shoper_id
            category.shoper_category_is_root = shoper_category_is_root
            category.shoper_order = shoper_order
            category.save()
            print(f"!!Category updated: {category.shoper_id}")
        else:
            print(f"No Updates for Category: {category.shoper_id}")
    except Category.DoesNotExist:
        category = Category.objects.create(
            shoper_id=shoper_id,
            shoper_category_is_root=shoper_category_is_root,
            shoper_order=shoper_order,
        )
        print(f"Category created: {category.shoper_id}")

    return category
