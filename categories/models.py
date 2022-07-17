from django.db import models
from django.urls import reverse
from products.models import Product


class Category(models.Model):
    """Model for Category object."""

    shoper_id = models.IntegerField(unique=True, blank=True, null=True)
    shoper_category_is_root = models.IntegerField(blank=True, null=True)
    shoper_order = models.IntegerField(blank=True, null=True)
    # Local
    shoper_current_name = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shoper_products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return (
            f"Category ID:{self.shoper_id} ; Category Name:{self.shoper_current_name}"
        )

    def get_absolute_url(self):
        return reverse("categories:category-detail", kwargs={"pk": self.id})
