from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path("", include("panel.urls", namespace="panel")),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls", namespace="products")),
    path("categories/", include("categories.urls", namespace="categories")),
]
