from django.db import models
from translations.models import ImageTranslation
from django.core.validators import MinValueValidator, MaxValueValidator


class Image(models.Model):
    """Class for Image object."""

    # Shoper Data
    shoper_gfx_id = models.IntegerField(unique=True)
    shoper_product_id = models.IntegerField(blank=True, null=True)
    shoper_main = models.IntegerField(blank=True, null=True)

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
    shoper_image_name = models.CharField(max_length=255, blank=True)
    shoper_unic = models.CharField(max_length=255)
    shoper_hidden = models.CharField(max_length=1, blank=True, null=True)
    shoper_extension = models.CharField(max_length=5, blank=True, null=True)
    translations = models.ManyToManyField(ImageTranslation, blank=True)
    # shoper_csv_image_link = xxx
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ("-created",)

    def __str__(self):

        return f"ImageID:{self.shoper_gfx_id} | ProductID:{self.shoper_product_id}"
