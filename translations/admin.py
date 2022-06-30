from django.contrib import admin
from translations.models import (
    ProductTranslation,
    ImageTranslation,
    CategoryTranslation,
)


admin.site.register(ProductTranslation)
admin.site.register(ImageTranslation)
admin.site.register(CategoryTranslation)
