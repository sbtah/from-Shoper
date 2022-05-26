from django.db import models
from images.models import Image
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse


class Product(models.Model):
    """Model for Product object."""

    # Shoper Main Data
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_ean = models.CharField(max_length=13, blank=True)
    shoper_sku = models.CharField(max_length=25, unique=True, blank=True)
    shoper_vol_weight = models.CharField(max_length=100, blank=True)
    is_active_shoper = models.BooleanField(blank=True, null=True)  # proper field?
    created_shoper = models.CharField(max_length=50, blank=True, null=True)
    updated_shoper = models.CharField(max_length=50, blank=True, null=True)
    shoper_stock_price = models.CharField(max_length=40, blank=True)
    shoper_producer_id = models.IntegerField(blank=True, null=True)  # None ?
    shoper_category_id = models.IntegerField(blank=True, null=True)  # None ?
    shoper_delivery_id = models.IntegerField(blank=True, null=True)  # None ?
    shoper_other_price = models.CharField(max_length=40, blank=True)  #
    shoper_gauge_id = models.IntegerField(blank=True, null=True)
    shoper_bestseller_tag = models.BooleanField(blank=True, null=True)
    shoper_new_product_tag = models.BooleanField(blank=True, null=True)
    shoper_unit_id = models.IntegerField(blank=True, null=True)  # None
    shoper_currency_id = models.IntegerField(blank=True, null=True)  # None
    shoper_weight = models.CharField(max_length=5, blank=True, null=True)  # None
    shoper_availability_id = models.IntegerField(blank=True, null=True)  # None
    # Shoper Special Offer.
    shoper_promo_id = models.IntegerField(blank=True, null=True)
    shoper_promo_start = models.CharField(max_length=50, blank=True, null=True)
    shoper_promo_ends = models.CharField(max_length=50, blank=True, null=True)
    shoper_discount_value = models.CharField(max_length=50, blank=True, null=True)
    # PL SEO DATA
    shoper_title_pl = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_pl = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_pl = models.TextField(blank=True)  #
    shoper_description_pl = models.TextField(blank=True)
    shoper_seo_title_pl = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_pl = models.TextField(blank=True)
    shoper_permalink_pl = models.CharField(max_length=200, blank=True)
    shoper_seo_url_pl = models.CharField(max_length=200, blank=True)
    # GB SEO DATA
    shoper_title_gb = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_gb = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_gb = models.TextField(blank=True)  #
    shoper_description_gb = models.TextField(blank=True)
    shoper_seo_title_gb = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_gb = models.TextField(blank=True)
    shoper_permalink_gb = models.CharField(max_length=200, blank=True)
    shoper_seo_url_gb = models.CharField(max_length=200, blank=True)
    # EU SEO DATA
    shoper_title_eu = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_eu = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_eu = models.TextField(blank=True)  #
    shoper_description_eu = models.TextField(blank=True)
    shoper_seo_title_eu = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_eu = models.TextField(blank=True)
    shoper_permalink_eu = models.CharField(max_length=200, blank=True)
    shoper_seo_url_eu = models.CharField(max_length=200, blank=True)
    # FR SEO DATA
    shoper_title_fr = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_fr = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_fr = models.TextField(blank=True)  #
    shoper_description_fr = models.TextField(blank=True)
    shoper_seo_title_fr = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_fr = models.TextField(blank=True)
    shoper_permalink_fr = models.CharField(max_length=200, blank=True)
    shoper_seo_url_fr = models.CharField(max_length=200, blank=True)
    # DE SEO DATA
    shoper_title_de = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_de = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_de = models.TextField(blank=True)  #
    shoper_description_de = models.TextField(blank=True)
    shoper_seo_title_de = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_de = models.TextField(blank=True)
    shoper_permalink_de = models.CharField(max_length=200, blank=True)
    shoper_seo_url_de = models.CharField(max_length=200, blank=True)
    # US SEO DATA
    shoper_title_us = models.CharField(max_length=200, blank=True)
    shoper_translation_is_active_us = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_us = models.TextField(blank=True)  #
    shoper_description_us = models.TextField(blank=True)
    shoper_seo_title_us = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_us = models.TextField(blank=True)
    shoper_permalink_us = models.CharField(max_length=200, blank=True)
    shoper_seo_url_us = models.CharField(max_length=200, blank=True)
    # Shopify Data - Not used yet!
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    shopify_ean = models.CharField(max_length=13, blank=True)
    shopify_sku = models.CharField(max_length=25, blank=True)
    shopify_title = models.CharField(max_length=200, blank=True, null=True)
    shopify_description = models.TextField(blank=True, null=True)
    shopify_position = models.CharField(max_length=20, blank=True)
    is_active_shopify = models.CharField(max_length=1, blank=True)
    shopify_tags = models.CharField(max_length=200, blank=True)
    created_shopify = models.DateTimeField(blank=True, null=True)
    updated_shopify = models.DateTimeField(blank=True, null=True)
    shopify_price = models.CharField(max_length=40, blank=True)
    shopify_seo_title = models.CharField(max_length=200, blank=True)
    shopify_seo_description = models.TextField(blank=True)
    # Images Links from CSV
    shoper_url_image_1 = models.CharField(max_length=255, blank=True)
    shoper_url_image_2 = models.CharField(max_length=255, blank=True)
    shoper_url_image_3 = models.CharField(max_length=255, blank=True)
    shoper_url_image_4 = models.CharField(max_length=255, blank=True)
    shoper_url_image_5 = models.CharField(max_length=255, blank=True)
    shoper_url_image_6 = models.CharField(max_length=255, blank=True)
    shoper_url_image_7 = models.CharField(max_length=255, blank=True)
    shoper_url_image_8 = models.CharField(max_length=255, blank=True)
    # Local Data
    vendor_brand = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shoper_images = models.ManyToManyField(Image, blank=True)
    shoper_promo_price_calculated = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )

    shoper_tags = models.CharField(max_length=200, blank=True)

    def __repr__(self):
        return self.shoper_id

    def __str__(self):
        return f"ID:{self.shoper_id} | {self.shoper_title_pl}"

    def save(self, *args, **kwargs):
        """Custom save method that add related images to Product."""

        super().save(*args, **kwargs)
        images = Image.objects.all()
        for image in images:
            if image.shoper_product_id == self.shoper_id:
                self.shoper_images.add(image)
        if self.shoper_discount_value:
            self.shoper_promo_price_calculated = float(self.shoper_stock_price) - float(
                self.shoper_discount_value
            )

    def prepare_pl_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_pl,
            "shoper_translation_is_active": self.shoper_translation_is_active_pl,
            "shoper_short_description": self.shoper_short_description_pl,
            "shoper_description": self.shoper_description_pl,
        }

    def prepare_gb_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_gb,
            "shoper_translation_is_active": self.shoper_translation_is_active_gb,
            "shoper_short_description": self.shoper_short_description_gb,
            "shoper_description": self.shoper_description_gb,
        }

    def prepare_eu_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_eu,
            "shoper_translation_is_active": self.shoper_translation_is_active_eu,
            "shoper_short_description": self.shoper_short_description_eu,
            "shoper_description": self.shoper_description_eu,
        }

    def prepare_fr_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_fr,
            "shoper_translation_is_active": self.shoper_translation_is_active_fr,
            "shoper_short_description": self.shoper_short_description_fr,
            "shoper_description": self.shoper_description_fr,
        }

    def prepare_de_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_de,
            "shoper_translation_is_active": self.shoper_translation_is_active_de,
            "shoper_short_description": self.shoper_short_description_de,
            "shoper_description": self.shoper_description_de,
        }

    def prepare_us_copy_data(self):
        return {
            "shoper_translation_name": self.shoper_title_us,
            "shoper_translation_is_active": self.shoper_translation_is_active_us,
            "shoper_short_description": self.shoper_short_description_us,
            "shoper_description": self.shoper_description_us,
        }

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})


@receiver(m2m_changed, sender=Product.shoper_images.through)
def image_added_removed_product(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        # print(kwargs)
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
        for item in qs:
            item.shoper_product_id = instance.shoper_id
            item.save()

    elif action == "post_remove":
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
        for item in qs:
            item.shoper_product_id = ""
            item.order = ""
            item.shoper_main = False
            item.shoper_unic = ""
            item.save()
