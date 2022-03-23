from django.db import models
from images.models import Image


class Product(models.Model):
    """Model for Product object."""

    shoper_title_pl = models.CharField(max_length=200)  #
    shoper_title_en = models.CharField(max_length=200, blank=True)  #
    shoper_title_fr = models.CharField(max_length=200, blank=True)  #
    shoper_title_de = models.CharField(max_length=200, blank=True)  #
    shoper_description_pl = models.TextField(blank=True)  #
    shoper_description_en = models.TextField(blank=True)  #
    shoper_description_fr = models.TextField(blank=True)  #
    shoper_description_de = models.TextField(blank=True)  #

    shopify_title = models.CharField(max_length=200, blank=True, null=True)
    shopify_description = models.TextField(blank=True, null=True)

    vendor_brand = models.CharField(max_length=100, blank=True)  #
    shoper_id = models.IntegerField(unique=True)
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_ean = models.CharField(max_length=13, blank=True)  #
    shoper_sku = models.CharField(max_length=25, unique=True, blank=True)  #
    shopify_ean = models.CharField(max_length=13, blank=True)
    shopify_sku = models.CharField(max_length=25, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    shopify_position = models.IntegerField(blank=True, null=True)
    shoper_weight = models.CharField(max_length=100, blank=True)  #

    is_active_shoper = models.BooleanField(default=False)  #
    is_active_shopify = models.BooleanField(default=False)
    shoper_tags = models.CharField(max_length=200, blank=True)
    shopify_tags = models.CharField(max_length=200, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shoper = models.DateTimeField()  # add_date
    updated_shoper = models.DateTimeField(null=True)  # edit_date
    created_shopify = models.DateTimeField(null=True)
    updated_shopify = models.DateTimeField(null=True)
    shoper_price = models.CharField(max_length=40)  # price
    shoper_gauge_id = models.IntegerField(null=True)  # gauge_id
    shopify_seo_title = models.CharField(max_length=200, blank=True)
    shopify_seo_description = models.TextField(blank=True)

    def __str__(self):
        return f"Title-{self.shoper_title_pl};Shoper_ID-{self.shoper_id};Shopify_ID-{self.shopify_id}"
