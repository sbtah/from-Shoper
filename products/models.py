from django.db import models
from images.models import Image


class Product(models.Model):
    """Model for Product object."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    vendor = models.CharField(max_length=100)
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    ean = models.CharField(max_length=13, unique=True)
    sku = models.CharField(max_length=25, unique=True)
    images = models.ManyToManyField(Image, blank=True)
    shopify_position = models.IntegerField(blank=True, null=True)
    shoper_weight = models.IntegerField(blank=True, null=True)
    is_active_shoper = models.BooleanField(default=False)
    is_active_shopify = models.BooleanField(default=False)
    shopify_tags = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_shopify = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Title-{self.title};Shoper_ID-{self.shoper_id};Shopify_ID-{self.shopify_id}"
