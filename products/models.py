from django.db import models
from tags.models import Tag
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse


class Product(models.Model):
    """Model for Product object."""

    # Shoper Main Data
    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_type = models.IntegerField(blank=True, null=True)  # Implement in GET
    shoper_producer_id = models.IntegerField(blank=True, null=True)
    shoper_group_id = models.IntegerField(blank=True, null=True)  # Implement in GET
    shoper_tax_id = models.IntegerField(blank=True, null=True)  # Implement in GET
    shoper_category_id = models.IntegerField(blank=True, null=True)
    shoper_unit_id = models.IntegerField(blank=True, null=True)
    created_shoper = models.CharField(max_length=50, blank=True, null=True)
    updated_shoper = models.CharField(max_length=50, blank=True, null=True)
    shoper_other_price = models.CharField(max_length=40, blank=True, null=True)
    shoper_promo_price = models.CharField(
        max_length=40, blank=True, null=True
    )  # Implement in GET
    shoper_sku = models.CharField(max_length=25, unique=True, blank=True)
    shoper_ean = models.CharField(max_length=13, blank=True)
    shoper_pkwiu = models.CharField(max_length=100, blank=True)  # Implement in GET
    shoper_is_product_of_day = models.IntegerField(
        blank=True, null=True
    )  # Implement in GET
    shoper_bestseller_tag = models.BooleanField(blank=True, null=True)
    shoper_new_product_tag = models.BooleanField(blank=True, null=True)
    shoper_vol_weight = models.CharField(max_length=100, blank=True)
    shoper_gauge_id = models.IntegerField(blank=True, null=True)
    shoper_currency_id = models.IntegerField(blank=True, null=True)
    # Stock
    # Images
    # Translations
    # Shoper Special Offer.
    shoper_promo_id = models.IntegerField(blank=True, null=True)
    shoper_promo_start = models.CharField(max_length=50, blank=True, null=True)
    shoper_promo_ends = models.CharField(max_length=50, blank=True, null=True)
    shoper_discount_value = models.CharField(max_length=50, blank=True, null=True)
    # Local
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID-Shoper:{self.shoper_id} | SKU-Shoper:{self.shoper_sku}"

    # def save(self, *args, **kwargs):
    #     """Custom save method that add related images to Product."""

    #     super().save(*args, **kwargs)
    #     images = Image.objects.filter(shoper_product_if=self.shoper_id)
    #     translations = ProductTranslation.objects.filter(
    #         related_product_id=self.shoper_id
    #     )
    #     for image in images:
    #         if image.shoper_product_id == self.shoper_id:
    #             self.shoper_images.add(image)
    #     for translation in translations:
    #         if translation.related_product_id == self.shoper_id:
    #             self.shoper_product_translations.add(translation)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"pk": self.id})

    @property
    def shoper_product_images(self):
        return [
            translation.id
            for translation in Product.objects.get(id=self.id).image_set.all()
        ]

    # # CSV Image
    # @property!!! list of all stocks ids
    # shoper_product_stocks = models.ManyToManyField(Stock, blank=True)
    # Translations property!


# @receiver(m2m_changed, sender=Product.shoper_images.through)
# def image_added_removed_product(sender, instance, action, *args, **kwargs):
#     if action == "post_add":
#         # print(kwargs)
#         qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
#         for item in qs:
#             item.shoper_product_id = instance.shoper_id
#             item.save()

#     elif action == "post_remove":
#         qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
#         for item in qs:
#             item.shoper_product_id = ""
#             item.order = ""
#             item.shoper_main = False
#             item.shoper_unic = ""
#             item.save()
