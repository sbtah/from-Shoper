from django.contrib import admin
from translations.models import ProductTranslation, ImageTranslation


admin.site.register(ProductTranslation)
admin.site.register(ImageTranslation)
