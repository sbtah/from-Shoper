from django.db import models
from products.models import Product


class Stock(models.Model):
    """Model for Stock object."""

    shoper_stock_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_stock_product_id = models.IntegerField(blank=True, null=True)
    shoper_stock_related_product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True
    )
    shoper_stock_extended = models.IntegerField(blank=True, null=True)
    shoper_stock_price = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_active = models.IntegerField(blank=True, null=True)
    shoper_stock_default = models.IntegerField(blank=True, null=True)
    shoper_stock_value = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_warn_level = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_sold = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_code = models.CharField(max_length=25, blank=True)
    shoper_stock_ean = models.CharField(max_length=25, blank=True)
    shoper_stock_weight = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_weight_type = models.IntegerField(blank=True, null=True)
    shoper_stock_availability_id = models.IntegerField(blank=True, null=True)
    shoper_stock_delivery_id = models.IntegerField(blank=True, null=True)
    shoper_stock_gfx_id = models.IntegerField(blank=True, null=True)
    shoper_stock_package = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_price_wholesale = models.CharField(
        max_length=20, blank=True, null=True
    )
    shoper_stock_price_special = models.CharField(max_length=20, blank=True, null=True)
    shoper_stock_calculation_unit_id = models.IntegerField(blank=True, null=True)
    shoper_stock_calculation_unit_ratio = models.CharField(
        max_length=20, blank=True, null=True
    )
    # Local
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stock:{self.shoper_stock_id} For:{self.shoper_stock_product_id}"
