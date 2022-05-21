from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    """Class for Image object."""

    # Shoper Data
    shoper_gfx_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_product_id = models.IntegerField(blank=True, null=True)
    shoper_main = models.IntegerField(blank=True, null=True)
    shoper_title_pl = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_en = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_de = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_fr = models.CharField(max_length=100, blank=True, null=True)

    class Order(models.IntegerChoices):
        first = 1
        second = 2
        third = 3
        fourth = 4
        fifth = 5
        sixth = 6
        seventh = 7
        eighth = 8
        ninth = 9
        tenth = 10
        eleventh = 11
        twelfth = 12
        thirteenth = 13
        fourteenth = 14
        fifteenth = 15

    shoper_order = models.IntegerField(
        choices=Order.choices,
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        blank=True,
        null=True,
    )
    shoper_link_pl = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    shoper_link_en = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    shoper_link_de = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    shoper_link_fr = models.CharField(
        max_length=255, unique=True, blank=True, null=True
    )
    shoper_unic = models.CharField(max_length=255)
    shoper_hidden = models.CharField(max_length=1, blank=True, null=True)
    shoper_extension = models.CharField(max_length=5, blank=True, null=True)
    # Shopify Data
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    shopify_product_id = models.CharField(max_length=20, blank=True, null=True)
    shopify_link = models.CharField(max_length=255, unique=True, blank=True, null=True)
    # Local Data
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-created",)

    def __str__(self):

        return f"ImageID:{self.shoper_gfx_id} | {self.shoper_title_pl}"
