from django.db import models
from images.models import Image
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


class Product(models.Model):
    """Model for Product object."""

    shoper_title_pl = models.CharField(max_length=200)  #
    shoper_title_en = models.CharField(max_length=200, blank=True)  #
    shoper_title_fr = models.CharField(max_length=200, blank=True)  #
    shoper_title_de = models.CharField(max_length=200, blank=True)  #
    shoper_description_pl = models.TextField(blank=True)  #
    shoper_description_en = models.TextField(blank=True)  #
    shoper_description_fr = models.TextField(blank=True)  #
    shoper_description_de = models.TextField(blank=True)  #
    shopify_title = models.CharField(max_length=200, blank=True, null=True)
    shopify_description = models.TextField(blank=True, null=True)
    vendor_brand = models.CharField(max_length=100, blank=True)  #
    shoper_id = models.IntegerField(unique=True)
    shopify_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_ean = models.CharField(max_length=13, blank=True)  #
    shoper_sku = models.CharField(max_length=25, unique=True, blank=True)  #
    shopify_ean = models.CharField(max_length=13, blank=True)
    shopify_sku = models.CharField(max_length=25, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    shopify_position = models.IntegerField(blank=True, null=True)
    shoper_weight = models.CharField(max_length=100, blank=True)  #
    is_active_shoper = models.BooleanField(default=False)  #
    is_active_shopify = models.BooleanField(default=False)
    shoper_tags = models.CharField(max_length=200, blank=True)
    shopify_tags = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_shoper = models.DateTimeField(blank=True, null=True)  # add_date
    updated_shoper = models.DateTimeField(blank=True, null=True)  # edit_date
    created_shopify = models.DateTimeField(blank=True, null=True)
    updated_shopify = models.DateTimeField(blank=True, null=True)
    shoper_price = models.CharField(max_length=40, blank=True)  # price
    shopify_price = models.CharField(max_length=40, blank=True)
    shoper_gauge_id = models.IntegerField(blank=True, null=True)  # gauge_id
    shopify_seo_title = models.CharField(max_length=200, blank=True)
    shopify_seo_description = models.TextField(blank=True)
    is_on_shoper = models.BooleanField(default=False)
    is_on_shopify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.shoper_title_pl} ShoperID:{self.shoper_id} ShopifyID:{self.shopify_id}"

    def save(self, *args, **kwargs):
        """Custom save method that add related images to Product."""

        super().save(*args, **kwargs)
        images = Image.objects.all()
        for image in images:
            if image.shoper_product_id == self.shoper_id:
                self.images.add(image)


@receiver(m2m_changed, sender=Product.images.through)
def image_post_used(sender, instance, action, *args, **kwargs):
    if action == "post_add":
        # print(kwargs)
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
        for item in qs:
            item.shoper_product_id = instance.shoper_id
            item.save()

    elif action == "post_remove":
        qs = kwargs.get("model").objects.filter(pk__in=kwargs.get("pk_set"))
        for item in qs:
            item.shoper_product_id = None
            item.order = None
            item.shoper_main = False
            item.shoper_unic = False
            item.save()
