from shoper_api import (
    get_list_of_all_shoper_product_ids,
    get_product_data_for_shopify,
    get_list_of_all_shoper_image_ids,
)
from shopify_api import create_product

# print(get_list_of_all_shoper_product_ids())
print(get_product_data_for_shopify(222))
# print(get_list_of_all_shoper_image_ids())


# for x in get_list_of_all_shoper_image_ids():
#     print(x)
