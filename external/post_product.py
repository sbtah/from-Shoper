# import json
# import time
# import requests
# from external.get_token import SHOPER_STORE, TOKEN

# # from external.get_products import get_single_product_data_for_copy
# from external.create_url import create_seo_url


# # Create a copy of product!
# def create_single_product_for_laguage(from_id, from_language_code, to_language_code):
#     """Create a copy of product data specified by id and it's language code."""
#     """NOT USED IN ANY DJANGO LOGIC"""

#     # product = get_single_product_data_for_copy(from_id, from_language_code)

#     data = json.dumps(
#         {
#             "producer_id": product["producer_id"],
#             "category_id": f"{product['category_id']}",
#             "other_price": f"{product['other_price']}",
#             "code": f"{product['code']}{to_language_code[3:]}",
#             "ean": f"{product['ean']}",
#             "vol_weight": f"{product['vol_weight']}",
#             "stock": {
#                 "price": f"{product['stock_price']}",
#                 "weight": f"{product['stock_weight']}",
#                 # "availability_id": f"{'' if product['stock_availability_id'] == None else product['stock_availability_id']} ",
#                 "delivery_id": f"{product['stock_delivery_id']}",
#                 # "gfx_id": f"{'' if product['stock_gfx_id'] == None else product['stock_gfx_id']}",
#             },
#             "translations": {
#                 f"{to_language_code}": {
#                     "name": f"{product['translations_name']}",
#                     "short_description": f"{product['translations_short_description']}",
#                     "description": f"{product['translations_description']}",
#                     "active": f"{product['translations_active']}",
#                     "seo_title": f"",
#                     "seo_description": f"",
#                     "seo_keywords": f"",
#                     "seo_url": create_seo_url(
#                         to_language_code, product["translations_name"], from_id
#                     ),
#                 }
#             },
#         }
#     )

#     url = f"https://{SHOPER_STORE}/webapi/rest/products"
#     headers = {"Authorization": f"Bearer {TOKEN}"}
#     response = requests.post(url, headers=headers, data=data)
#     res = response.json()
#     time.sleep(0.5)

#     return res


# def create_copy_of_product_at_shoper(
#     shoper_sku,
#     to_language_code,
#     producer_id,
#     category_id,
#     other_price,
#     code,
#     ean,
#     shoper_vol_weight,
#     stock_price,
#     stock_weight,
#     stock_availability_id,
#     shoper_delivery_id,
#     translations_name,
#     translations_active,
#     translations_short_description,
#     translations_description,
# ):
#     """
#     USED IN DJANGO.
#     Sends a POST request with Product Data to Shoper's product endpoint.
#     Creates a NEW Product and returns JSON response after.
#     """
#     seo_url = create_seo_url(to_language_code, translations_name, shoper_sku)
#     data = json.dumps(
#         {
#             "producer_id": producer_id,
#             "category_id": category_id,
#             "other_price": other_price,
#             "code": f"{code}{to_language_code[3:]}",
#             "ean": ean,
#             "vol_weight": shoper_vol_weight,
#             "stock": {
#                 "price": stock_price,
#                 "weight": stock_weight,
#                 "availability_id": stock_availability_id,
#                 "delivery_id": shoper_delivery_id,
#             },
#             "translations": {
#                 f"{to_language_code}": {
#                     "name": translations_name,
#                     "short_description": translations_short_description,
#                     "description": translations_description,
#                     "active": translations_active,
#                     "seo_title": "",
#                     "seo_description": "",
#                     "seo_keywords": "",
#                     "seo_url": seo_url,
#                 }
#             },
#         }
#     )
#     url = f"https://{SHOPER_STORE}/webapi/rest/products"
#     headers = {"Authorization": f"Bearer {TOKEN}"}
#     response = requests.post(url, headers=headers, data=data)
#     res = response.json()
#     time.sleep(0.5)

#     return res, seo_url
