from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    """Class for Image object."""

    shoper_gfx_id = models.CharField(max_length=20, unique=True)
    shopify_id = models.CharField(max_length=20, blank=True, null=True)
    shoper_product_id = models.CharField(max_length=20, blank=True, null=True)
    shopify_product_id = models.CharField(max_length=20, blank=True, null=True)
    shoper_main = models.BooleanField(default=False)
    shoper_title_pl = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_en = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_de = models.CharField(max_length=100, blank=True, null=True)
    shoper_title_fr = models.CharField(max_length=100, blank=True, null=True)

    class Order(models.TextChoices):
        first = "1"
        second = "2"
        third = "3"
        fourth = "4"
        fifth = "5"
        sixth = "6"
        seventh = "7"
        eighth = "8"
        ninth = "9"
        tenth = "10"
        eleventh = "11"
        twelfth = "12"
        thirteenth = "13"
        fourteenth = "14"
        fifteenth = "15"

    order = models.CharField(
        choices=Order.choices,
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        max_length=2,
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
    shopify_link = models.CharField(max_length=255, unique=True, blank=True, null=True)
    shoper_unic = models.CharField(max_length=255, unique=True)
    hidden = models.BooleanField(default=False)
    extension = models.CharField(max_length=3, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-created",)

    def __str__(self):

        return f"GFX-ID:{self.shoper_gfx_id} Product-ID:{self.shoper_product_id}"
