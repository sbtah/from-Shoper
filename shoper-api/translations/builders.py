from products.models import Product
from categories.models import Category
from images.models import Image
from translations.models import (
    ProductTranslation,
    CategoryTranslation,
    ImageTranslation,
)
from apiclient.helpers.logging import logging


# TODO
# Implement logs mechanic to store changes on models done on Store.
# Test data coming from call vs stored on model


def update_or_create_category_translation(
    locale,
    shoper_translation_id,
    related_category_id,
    name,
    description,
    description_bottom,
    seo_title,
    seo_description,
    seo_keywords,
    seo_url,
    permalink,
    active,
    is_default,
    lang_id,
    items,
):
    """Create or Update an instance of CategoryTranslation object with data coming from API call to Shoper's store."""
    try:
        category_translation = CategoryTranslation.objects.get(
            shoper_translation_id=shoper_translation_id,
        )
        if (
            str(related_category_id) != str(category_translation.related_category_id)
            or (str(name) != str(category_translation.name))
            or (str(description) != str(category_translation.description))
            or (str(description_bottom) != str(category_translation.description_bottom))
            or (str(seo_title) != str(category_translation.seo_title))
            or (str(seo_description) != str(category_translation.seo_description))
            or (str(seo_keywords) != str(category_translation.seo_keywords))
            or (str(seo_url) != str(category_translation.seo_url))
            or (str(permalink) != str(category_translation.permalink))
            or (str(active) != str(category_translation.active))
            or (str(is_default) != str(category_translation.is_default))
            or (str(lang_id) != str(category_translation.lang_id))
            or (str(items) != str(category_translation.items))
        ):
            category_translation.related_category_id = related_category_id
            category_translation.name = name
            category_translation.description = description
            category_translation.description_bottom = description_bottom
            category_translation.seo_title = seo_title
            category_translation.seo_description = seo_description
            category_translation.seo_keywords = seo_keywords
            category_translation.seo_url = seo_url
            category_translation.permalink = permalink
            category_translation.active = active
            category_translation.is_default = is_default
            category_translation.lang_id = lang_id
            category_translation.items = items
            category_translation.save()

            parrent_category = Category.objects.get(shoper_id=related_category_id)
            parrent_category.categorytranslation_set.add(category_translation)
            logging.info(
                f"!! UPDATE CategoryTranslation: {category_translation.shoper_translation_id} for Category: {parrent_category}"
            )
        else:
            parrent_category = Category.objects.get(shoper_id=related_category_id)
            parrent_category.categorytranslation_set.add(category_translation)
            logging.info(
                f"NO UPDATE CategoryTranslation: {category_translation.shoper_translation_id} for Category: {parrent_category}"
            )
    except CategoryTranslation.DoesNotExist:
        category_translation = CategoryTranslation.objects.create(
            locale=locale,
            shoper_translation_id=shoper_translation_id,
            related_category_id=related_category_id,
            name=name,
            description=description,
            description_bottom=description_bottom,
            seo_title=seo_title,
            seo_description=seo_description,
            seo_keywords=seo_keywords,
            seo_url=seo_url,
            permalink=permalink,
            active=active,
            is_default=is_default,
            lang_id=lang_id,
            items=items,
        )
        parrent_category = Category.objects.get(shoper_id=related_category_id)
        parrent_category.categorytranslation_set.add(category_translation)
        logging.info(
            f"!! CREATE CategoryTranslation: {category_translation.shoper_translation_id} for Category: {parrent_category}"
        )
    return category_translation


def update_or_create_product_translation(
    locale,
    shoper_translation_id,
    related_product_id,
    name,
    short_description,
    description,
    active,
    is_default,
    lang_id,
    seo_title,
    seo_description,
    seo_keywords,
    seo_url,
    permalink,
    order,
    main_page,
    main_page_order,
):
    """Create or Update an instance of ProductTranslation object with data coming from API call to Shoper's store."""
    try:
        translation = ProductTranslation.objects.get(
            shoper_translation_id=shoper_translation_id
        )
        """
        Checks is data translation data in DB is not different from response.
        If there is a difference on one of the fields, model is updated.
        """
        if (
            (str(translation.locale) != str(locale))
            or (str(translation.shoper_translation_id) != str(shoper_translation_id))
            or (str(translation.related_product_id) != str(related_product_id))
            or (str(translation.name) != str(name))
            or (str(translation.short_description) != str(short_description))
            or (str(translation.description) != str(description))
            or (str(translation.active) != str(active))
            or (str(translation.is_default) != str(is_default))
            or (str(translation.lang_id) != str(lang_id))
            or (str(translation.seo_title) != str(seo_title))
            or (str(translation.seo_description) != str(seo_description))
            or (str(translation.seo_keywords) != str(seo_keywords))
            or (str(translation.seo_url) != str(seo_url))
            or (str(translation.permalink) != str(permalink))
            or (str(translation.order) != str(order))
            or (str(translation.main_page) != str(main_page))
            or (str(translation.main_page_order) != str(main_page_order))
        ):

            translation.locale = locale
            translation.shoper_translation_id = shoper_translation_id
            translation.related_product_id = related_product_id
            translation.name = name
            translation.short_description = short_description
            translation.description = description
            translation.active = active
            translation.is_default = is_default
            translation.lang_id = lang_id
            translation.seo_title = seo_title
            translation.seo_description = seo_description
            translation.seo_keywords = seo_keywords
            translation.seo_url = seo_url
            translation.permalink = permalink
            translation.order = order
            translation.main_page = main_page
            translation.description = description
            translation.main_page_order = main_page_order

            parrent_product = Product.objects.get(
                shoper_id=translation.related_product_id
            )
            parrent_product.producttranslation_set.add(translation)
            translation.save()
            logging.info(
                f"!! UPDATE ProductTranslation: {translation.shoper_translation_id} Updated"
            )
        else:
            parrent_product = Product.objects.get(
                shoper_id=translation.related_product_id
            )
            parrent_product.producttranslation_set.add(translation)

            logging.info(
                f"NO UPDATE for ProductTranslation: {translation.shoper_translation_id}"
            )
    except ProductTranslation.DoesNotExist:
        translation = ProductTranslation.objects.create(
            locale=locale,
            shoper_translation_id=shoper_translation_id,
            related_product_id=related_product_id,
            name=name,
            short_description=short_description,
            description=description,
            active=active,
            is_default=is_default,
            lang_id=lang_id,
            seo_title=seo_title,
            seo_description=seo_description,
            seo_keywords=seo_keywords,
            seo_url=seo_url,
            permalink=permalink,
            order=order,
            main_page=main_page,
            main_page_order=main_page_order,
        )
        parrent_product = Product.objects.get(shoper_id=translation.related_product_id)
        parrent_product.producttranslation_set.add(translation)
        logging.info(
            f"!! CREATE ProductTranslation: {translation.shoper_translation_id}"
        )
    return translation


def update_or_create_image_translation(
    locale,
    shoper_translation_id,
    related_gfx_id,
    name,
    lang_id,
):
    """Create or Update an instance of ImageTranslation object with data coming from API call to Shoper's store."""
    try:
        translation = ImageTranslation.objects.get(
            shoper_translation_id=shoper_translation_id
        )
        if (
            (str(translation.shoper_translation_id) != str(shoper_translation_id))
            or (str(related_gfx_id) != str(related_gfx_id))
            or (str(name) != str(name))
            or (str(lang_id) != str(lang_id))
        ):
            translation.shoper_translation_id = shoper_translation_id
            translation.related_gfx_id = related_gfx_id
            translation.name = name
            translation.lang_id = lang_id

            parrent_image = Image.objects.get(shoper_gfx_id=translation.related_gfx_id)
            parrent_image.imagetranslation_set.add(translation)
            translation.save()

            logging.info(f"!! UPDATE ImageTranslation: {translation}")
        else:
            logging.info(f"NO UPDATE for ImageTranslation: {translation}")
            parrent_image = Image.objects.get(shoper_gfx_id=translation.related_gfx_id)
            parrent_image.imagetranslation_set.add(translation)
    except ImageTranslation.DoesNotExist:
        translation = ImageTranslation.objects.create(
            locale=locale,
            shoper_translation_id=shoper_translation_id,
            related_gfx_id=related_gfx_id,
            name=name,
            lang_id=lang_id,
        )
        parrent_image = Image.objects.get(shoper_gfx_id=translation.related_gfx_id)
        parrent_image.imagetranslation_set.add(translation)
        logging.info(f"!! CREATE ImageTranslation: {translation}")
    return translation
