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
