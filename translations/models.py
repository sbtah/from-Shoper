from django.db import models


class Translation(models.Model):
    """"""

    locale = models.CharField(max_length=20)
    shoper_translation_id = models.IntegerField(unique=True)

    class Meta:
        abstract = True


class ProductTranslation(Translation):
    """"""

    related_product_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    active = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    lang_id = models.IntegerField(blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    seo_keywords = models.TextField(blank=True)
    seo_url = models.CharField(max_length=255, unique=True, blank=True)
    permalink = models.CharField(max_length=255, unique=True)
    order = models.IntegerField(blank=True, null=True)
    main_page = models.IntegerField(blank=True, null=True)
    main_page_order = models.IntegerField(blank=True, null=True)
    # Local
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.related_product_id}:{self.name}"


class ImageTranslation(Translation):
    """"""

    related_gfx_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    lang_id = models.IntegerField(blank=True, null=True)
    # Local
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.related_gfx_id}:{self.name}"
