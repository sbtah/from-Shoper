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
    active = models.BooleanField()
    is_default = models.BooleanField()
    lang_id = models.IntegerField()
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    seo_keywords = models.TextField(blank=True)
    seo_url = models.CharField(max_length=255, blank=True)
    permalink = models.CharField(max_length=255)
    order = models.IntegerField()
    main_page = models.BooleanField()
    main_page_order = models.IntegerField()
    # Local
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.related_product_id}:{self.name}"


# translations: {
#     (locale): {
#     translation_id: integer,
#     product_id: integer,
#     name: string,
#     short_description: string,
#     description: string,
#     active: boolean,
#     isdefault: boolean,
#     lang_id: integer,
#     seo_title: string,
#     seo_description: string,
#     seo_keywords: string,
#     seo_url: string|null,
#     permalink: string,
#     order: integer,
#     main_page: boolean,
#     main_page_order: integer
#     }
# },
