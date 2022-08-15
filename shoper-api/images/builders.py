from images.models import Image
from products.models import Product
from apiclient.helpers.logging import logging


def update_or_create_image(
    shoper_gfx_id,
    shoper_product_id,
    shoper_main,
    shoper_order,
    shoper_image_name,
    shoper_unic,
    shoper_hidden,
    shoper_extension,
):
    """Create or Update an instance of Image object from items provided from API call to Shoper API."""
    try:
        image = Image.objects.get(
            shoper_gfx_id=shoper_gfx_id,
        )
        if (
            (str(image.shoper_gfx_id) != str(shoper_gfx_id))
            or (str(image.shoper_product_id) != str(shoper_product_id))
            or (str(image.shoper_main) != str(shoper_main))
            or (str(image.shoper_order) != str(shoper_order))
            or (str(image.shoper_image_name) != str(shoper_image_name))
            or (str(image.shoper_unic) != str(shoper_unic))
            or (str(image.shoper_hidden) != str(shoper_hidden))
            or (str(image.shoper_extension) != str(shoper_extension))
        ):
            image.shoper_gfx_id = shoper_gfx_id
            image.shoper_product_id = shoper_product_id
            image.shoper_main = shoper_main
            image.shoper_order = shoper_order
            image.shoper_image_name = shoper_image_name
            image.shoper_unic = shoper_unic
            image.shoper_hidden = shoper_hidden
            image.shoper_extension = shoper_extension
            try:
                parrent_product = Product.objects.get(shoper_id=image.shoper_product_id)
                parrent_product.image_set.add(image)
            except Product.DoesNotExist:
                logging.info("!!! MISSING:: Parrent object does not exist.")
                pass
            finally:
                image.save()
                logging.info(f"! UPDATE Image: {image}")
        else:
            parrent_product = Product.objects.get(shoper_id=image.shoper_product_id)
            parrent_product.image_set.add(image)
            image.save()
            logging.info(f"NO UPDATE for Image: {image}")
    except Image.DoesNotExist:
        image = Image.objects.create(
            shoper_gfx_id=shoper_gfx_id,
            shoper_product_id=shoper_product_id,
            shoper_main=shoper_main,
            shoper_order=shoper_order,
            shoper_image_name=shoper_image_name,
            shoper_unic=shoper_unic,
            shoper_hidden=shoper_hidden,
            shoper_extension=shoper_extension,
        )
        try:
            parrent_product = Product.objects.get(shoper_id=image.shoper_product_id)
            parrent_product.image_set.add(image)
        except Product.DoesNotExist:
            logging.error("!!! MISSING:: Parrent object does not exist.")
            pass
        finally:
            image.save()
            logging.info(f"! CREATE Image: {Image}")
    except Exception as e:
        logging.info(f"!! Some other Exception: {e}")
    return image
