from django.db import models


class Stock(models.Model):
    """Model for Stock object."""

    shoper_stock_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_stock_product_id = models.IntegerField(blank=True, null=True)
    shoper_stock_extended = models.IntegerField(blank=True, null=True)
    shoper_stock_price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_active = models.IntegerField(blank=True, null=True)
    shoper_stock_default = models.IntegerField(blank=True, null=True)
    shoper_stock_value = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_warn_level = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_sold = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_code = models.CharField(max_length=25, unique=True, blank=True)
    shoper_stoc_ean = models.CharField(max_length=25, unique=True, blank=True)
    shoper_stock_weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_weight_type = models.IntegerField(blank=True, null=True)
    shoper_stock_availability_id = models.IntegerField(blank=True, null=True)
    shoper_stock_delivery_id = models.IntegerField(blank=True, null=True)
    shoper_stock_gfx_id = models.IntegerField(blank=True, null=True)
    shoper_stock_package = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_price_wholesale = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_price_special = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    shoper_stock_calculation_unit_id = models.IntegerField(blank=True, null=True)
    shoper_stock_calculation_unit_ratio = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True
    )
    # Local
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
