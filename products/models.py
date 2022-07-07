from django.db import models
from tags.models import Tag
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    """Model for Product object."""

    # Shoper Main Data
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_type = models.IntegerField(blank=True, null=True)
    shoper_producer_id = models.IntegerField(blank=True, null=True)
    shoper_group_id = models.IntegerField(blank=True, null=True)
    shoper_tax_id = models.IntegerField(blank=True, null=True)
    shoper_main_category_id = models.IntegerField(blank=True, null=True)
    shoper_all_categories_ids = ArrayField(models.IntegerField(blank=True, null=True))
    # This will have to be changed to M2M to work with many categories.
    shoper_unit_id = models.IntegerField(blank=True, null=True)
    created_shoper = models.CharField(max_length=50, blank=True, null=True)
    updated_shoper = models.CharField(max_length=50, blank=True, null=True)
    shoper_other_price = models.CharField(max_length=40, blank=True, null=True)
    shoper_promo_price = models.CharField(max_length=40, blank=True, null=True)
    shoper_sku = models.CharField(max_length=25, unique=True, blank=True)
    shoper_ean = models.CharField(max_length=13, blank=True)
    shoper_pkwiu = models.CharField(max_length=100, blank=True)
    shoper_is_product_of_day = models.IntegerField(blank=True, null=True)
    shoper_bestseller_tag = models.BooleanField(blank=True, null=True)
    shoper_new_product_tag = models.BooleanField(blank=True, null=True)
    shoper_vol_weight = models.CharField(max_length=100, blank=True)
    shoper_gauge_id = models.IntegerField(blank=True, null=True)
    shoper_currency_id = models.IntegerField(blank=True, null=True)
    shoper_promo_id = models.IntegerField(blank=True, null=True)
    shoper_promo_start = models.CharField(max_length=50, blank=True, null=True)
    shoper_promo_ends = models.CharField(max_length=50, blank=True, null=True)
    shoper_discount_value = models.CharField(max_length=50, blank=True, null=True)
    # TODO
    # Implement this field to work with array of categories that comes from API Response.
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID-Shoper:{self.shoper_id} | SKU-Shoper:{self.shoper_sku}"

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})
