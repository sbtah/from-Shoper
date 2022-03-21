from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    """Class for Image object."""

    shoper_id = models.CharField(max_length=20, unique=True)
    shopify_id = models.CharField(max_length=20, blank=True, null=True)
    shoper_product_id = models.CharField(max_length=20, blank=True, null=True)
    shopify_product_id = models.CharField(max_length=20, blank=True, null=True)
    shoper_main = models.BooleanField(default=False)

    class Order(models.IntegerChoices):
        first = 1
        second = 2
        third = 3
        fourth = 4
        fifth = 5
        sixth = 6
        seventh = 7
        eighth = 8

    order = models.IntegerField(
        choices=Order.choices, validators=[MinValueValidator(1), MaxValueValidator(15)]
    )
    shoper_link = models.CharField(max_length=255, unique=True, blank=True, null=True)
    shopify_link = models.CharField(max_length=255, unique=True, blank=True, null=True)
    shoper_unic = models.CharField(max_length=255, unique=True)
    hidden = models.BooleanField(default=False)
    extension = models.CharField(max_length=3, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-created",)

    def __str__(self):

        return f"ID {self.id};Shoper ID {self.shoper_id};Shopify ID {self.shopify_id};Product ID {self.product_id}"
