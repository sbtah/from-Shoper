from email.mime import image
from django.db import models


class Product(models.Model):
    """Model for Product object."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    vendor = models.CharField(max_length=100)
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    ean = models.CharField(max_length=13, unique=True)
    sku = models.CharField(max_length=25, unique=True)
