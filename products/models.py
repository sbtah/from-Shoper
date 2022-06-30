from django.db import models
from tags.models import Tag
from django.urls import reverse
from categories.models import Category


class Product(models.Model):
    """Model for Product object."""

    # Shoper Main Data
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_type = models.IntegerField(blank=True, null=True)
    shoper_producer_id = models.IntegerField(blank=True, null=True)
    shoper_group_id = models.IntegerField(blank=True, null=True)
    shoper_tax_id = models.IntegerField(blank=True, null=True)
    shoper_category_id = models.IntegerField(blank=True, null=True)
    shoper_related_category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
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
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID-Shoper:{self.shoper_id} | SKU-Shoper:{self.shoper_sku}"

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})
