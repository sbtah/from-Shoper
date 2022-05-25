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
    shoper_weight = models.CharField(max_length=100, blank=True)
    is_active_shoper = models.BooleanField(blank=True, null=True)  # proper field?
    vendor_brand = models.CharField(max_length=100, blank=True)
    created_shoper = models.CharField(max_length=50, blank=True, null=True)
    updated_shoper = models.CharField(max_length=50, blank=True, null=True)
    shoper_price = models.CharField(max_length=40, blank=True)

    # Need to implement few new fields.
    shoper_producer_id = models.IntegerField(blank=True, null=True)  #
    shoper_category_id = models.IntegerField(blank=True, null=True)  #
    shoper_delivery_id = models.IntegerField(blank=True, null=True)  #
    shoper_other_price = models.CharField(max_length=40, blank=True)  #

    shoper_gauge_id = models.CharField(max_length=20, blank=True, null=True)
    shoper_discount_value = models.CharField(max_length=10, blank=True)
    shoper_promo_id = models.IntegerField(blank=True, null=True)
    shoper_promo_start = models.CharField(max_length=50, blank=True, null=True)
    shoper_promo_ends = models.CharField(max_length=50, blank=True, null=True)
    shoper_bestseller_tag = models.BooleanField(blank=True, null=True)
    shoper_new_product_tag = models.BooleanField(blank=True, null=True)
    # Shoper - Not Api Calls
    shoper_promo_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    shoper_images = models.ManyToManyField(Image, blank=True)
    shoper_tags = models.CharField(max_length=200, blank=True)  # M2M ? not used now..
    # Updated from Shoper CSV File.
    shoper_url_image_1 = models.CharField(max_length=255, blank=True)
    shoper_url_image_2 = models.CharField(max_length=255, blank=True)
    shoper_url_image_3 = models.CharField(max_length=255, blank=True)
    shoper_url_image_4 = models.CharField(max_length=255, blank=True)
    shoper_url_image_5 = models.CharField(max_length=255, blank=True)
    shoper_url_image_6 = models.CharField(max_length=255, blank=True)
    shoper_url_image_7 = models.CharField(max_length=255, blank=True)
    shoper_url_image_8 = models.CharField(max_length=255, blank=True)
    # Titles all languages.
    shoper_title_pl = models.CharField(max_length=200)
    shoper_title_en = models.CharField(max_length=200, blank=True)
    shoper_title_fr = models.CharField(max_length=200, blank=True)
    shoper_title_de = models.CharField(max_length=200, blank=True)
    # PL SEO DATA
    shoper_translation_us_active_pl = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_pl = models.TextField(blank=True)  #
    shoper_description_pl = models.TextField(blank=True)
    shoper_seo_title_pl = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_pl = models.TextField(blank=True)
    shoper_permalink_pl = models.CharField(max_length=200, blank=True)
    shoper_seo_url_pl = models.CharField(max_length=200, blank=True)
    # EN SEO DATA
    shoper_translation_us_active_en = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_en = models.TextField(blank=True)  #
    shoper_description_en = models.TextField(blank=True)
    shoper_seo_title_en = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_en = models.TextField(blank=True)
    shoper_permalink_en = models.CharField(max_length=200, blank=True)
    shoper_seo_url_en = models.CharField(max_length=200, blank=True)
    # FR SEO DATA
    shoper_translation_us_active_fr = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_fr = models.TextField(blank=True)  #
    shoper_description_fr = models.TextField(blank=True)
    shoper_seo_title_fr = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_fr = models.TextField(blank=True)
    shoper_permalink_fr = models.CharField(max_length=200, blank=True)
    shoper_seo_url_fr = models.CharField(max_length=200, blank=True)
    # DE SEO DATA
    shoper_translation_us_active_de = models.BooleanField(blank=True, null=True)  #
    shoper_short_description_de = models.TextField(blank=True)  #
    shoper_description_de = models.TextField(blank=True)
    shoper_seo_title_de = models.CharField(max_length=200, blank=True)
    shoper_meta_desc_de = models.TextField(blank=True)
    shoper_permalink_de = models.CharField(max_length=200, blank=True)
    shoper_seo_url_de = models.CharField(max_length=200, blank=True)
    # US SEO DATA
    shoper_translation_us_active_us = models.BooleanField(blank=True, null=True)  #
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
    # Local Data
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
            self.shoper_promo_price = float(self.shoper_price) - float(
                self.shoper_discount_value
            )

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
